from trakteer_dev import Client

client = Client("hash", "streamkey")

@client.event
async def on_connect(ws):
    print("Connected to Trakteer!")

@client.event
async def on_donation(ws, data):
    print("Received donation:")
    print(f"  - Name: {data.name}")
    print(f"  - Amount: {data.amount}")
    print(f"  - Message: {data.message}")

client.start()
