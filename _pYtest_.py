from unittest.mock import AsyncMock, patch

import pytest

from trakteer_dev import Client, TrakteerDonationData


@pytest.fixture
def donation_data():
    return {
        "supporter_name": "John Doe",
        "unit": "Coffee",
        "quantity": 5,
        "supporter_message": "Keep up the great work!",
        "supporter_avatar": "https://example.com/avatar.jpg",
        "unit_icon": "☕",
        "price": "10.00",
        "media": "https://example.com/media.jpg",
        "id": "12345",
    }


def test_trakteer_donation_data_init(donation_data):
    data = TrakteerDonationData(donation_data)
    assert data.name == "John Doe"
    assert data.unit == "Coffee"
    assert data.amount == 5
    assert data.message == "Keep up the great work!"
    assert data.avatar == "https://example.com/avatar.jpg"
    assert data.unit_icon == "☕"
    assert data.price == "10.00"
    assert data.media == "https://example.com/media.jpg"
    assert data.id == "12345"


def test_trakteer_donation_data_to_dict(donation_data):
    data = TrakteerDonationData(donation_data)
    result = data.to_dict()
    assert result == {
        "name": "John Doe",
        "unit": "Coffee",
        "amount": 5,
        "message": "Keep up the great work!",
        "avatar": "https://example.com/avatar.jpg",
        "unit_icon": "☕",
        "price": "10.00",
        "media": "https://example.com/media.jpg",
        "id": "12345",
    }


@pytest.fixture
def client_mock():
    with patch("Client.wsconnect.connect", new_callable=AsyncMock) as mock_ws:
        yield mock_ws


def test_client_init():
    client = Client(userHash="dummyHash", streamKey="dummyKey", block=True, test=False)
    assert client.hash == "dummyHash"
    assert client.streamKey == "dummyKey"
    assert client.block is True
    assert client.test is False


@pytest.mark.asyncio
async def test_client_start(client_mock):
    client = Client(userHash="dummyHash", streamKey="dummyKey")
    with patch("Client.asyncio.run", side_effect=lambda x: x()):
        client.start()
        assert client_mock.call_count > 0


def test_missing_userhash():
    with pytest.raises(Exception, match="Missing user hash"):
        Client(streamKey="dummyKey")


def test_missing_streamkey():
    with pytest.raises(Exception, match="Missing stream key"):
        Client(userHash="dummyHash")
