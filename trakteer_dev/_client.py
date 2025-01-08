# ############################################
#
#        Trakteer Donate Client Library
#          ~~ 2023 (c) by Realzzy ~~
#           2025 Recode by ©Lucifer
#
# ############################################


import asyncio
import json
import os
import traceback
from threading import Thread

import websockets

from ._exception import (TrakteerMethodUnoverridable, TrakteerMissingStreamKey,
                         TrakteerMissingUserHash, TrakteerWebsocketError)
from ._logger import logger


class Client:
    """
    Client to handle Trakteer donation events

    Available methods to override:
    - on_connect(ws): Called when websocket is connected
    - on_close(ws, e): Called when websocket is closed
    - on_error(ws, e): Called when websocket returns error
    - on_donation(data): Called when donation is received
    - on_message(data): Called when raw message received

    2023 (c) by Realzzy
    2025 Recode by ©Lucifer
    """

    def __init__(self, userHash=None, streamKey=None, block=True, test=False):
        userHash = userHash or os.getenv("TRAKTEER_USERHASH")
        if not userHash:
            raise TrakteerMissingUserHash(
                "Missing user hash! Please provide user hash or set TRAKTEER_USERHASH environment variable."
            )

        streamKey = streamKey or os.getenv("TRAKTEER_STREAMKEY")
        if not streamKey:
            raise TrakteerMissingStreamKey(
                "Missing stream key! Please provide stream key or set TRAKTEER_STREAMKEY environment variable."
            )

        if streamKey.startswith("trstream-"):
            logger.warning(
                "Ignoring 'trstream-' prefix in stream key. Please remove it in the future."
            )
            streamKey = streamKey[9:]

        self.ws = None
        self.hash = str(userHash)
        self.streamKey = str(streamKey)

        self.block = block if isinstance(block, bool) else True
        if not isinstance(block, bool):
            logger.warning("'block' argument is not a boolean! Defaulting to True...")

        self.test = test if isinstance(test, bool) else False
        if not isinstance(test, bool):
            logger.warning("'test' argument is not a boolean! Defaulting to False...")

        self.has_connected = False
        self.subs_succed = False

    async def wsconnect(self):
        try:
            async with websockets.connect(
                "wss://socket.trakteer.id/app/2ae25d102cc6cd41100a?protocol=7&client=js&version=5.1.1&flash=false"
            ) as ws:
                self.ws = ws
                while True:
                    try:
                        data = await ws.recv()
                        await self.__parse_message(data)
                    except websockets.exceptions.ConnectionClosedError as e:
                        await self.on_close(ws, e)
                        break
                    except BaseException as e:
                        await self.on_error(ws, e)
                        break
        except BaseException as e:
            message = f"Can't connect to websocket: {str(e)}"
            if self.has_connected:
                message = "Websocket returned error"
            raise TrakteerWebsocketError(f"{message}:\n{traceback.format_exc()}")

    def start(self, **kwargs):
        if self.block:
            asyncio.run(self.wsconnect())
        else:
            Thread(target=lambda: asyncio.run(self.wsconnect())).start()

    async def __connected(self):
        await self.ws.send(
            json.dumps(
                {
                    "event": "pusher:subscribe",
                    "data": {
                        "auth": "",
                        "channel": f"creator-stream.{self.hash}.trstream-{self.streamKey}",
                    },
                }
            )
        )

        if self.test:
            await self.ws.send(
                json.dumps(
                    {
                        "event": "pusher:subscribe",
                        "data": {
                            "auth": "",
                            "channel": f"creator-stream-test.{self.hash}.trstream-{self.streamKey}",
                        },
                    }
                )
            )

        async def ping():
            while True:
                await asyncio.sleep(10)
                await self.ws.send(json.dumps({"event": "pusher:ping", "data": {}}))
                logger.debug("Sent ping to websocket")

        async def check_subs():
            if self.subs_succed:
                asyncio.create_task(ping())
                if not self.has_connected:
                    await self.on_connect(self.ws)
                    self.has_connected = True
            else:
                await asyncio.sleep(1)
                await check_subs()

        asyncio.create_task(check_subs())

    async def __parse_message(self, rawdata):
        try:
            data = json.loads(rawdata)
        except json.decoder.JSONDecodeError:
            logger.warn("Can't parse message received from websocket. Ignoring...")
        else:
            if data["event"] == "pusher:connection_established":
                await self.__connected()
            elif data["event"] == "pusher_internal:subscription_succeeded":
                self.subs_succed = True
            elif "BroadcastNotificationCreated" in data["event"]:
                await self.on_donation(data["data"])

            await self.on_message(data)

    async def on_connect(self, ws):
        pass

    async def on_close(self, ws, e):
        pass

    async def on_error(self, ws, e):
        pass

    async def on_donation(self, data):
        pass

    async def on_message(self, data):
        pass

    @classmethod
    def event(cls, func):
        if func.__name__ in ["__connected", "__parse_message"]:
            raise TrakteerMethodUnoverridable(
                f"Method '{func.__name__}' is unoverridable!"
            )

        setattr(cls, func.__name__, func)
        return func
