from unittest.mock import patch

from src.external_api import get_exchange_rate, get_share_price


@patch("requests.request")
def test_get_share_price(mock_get):
    mock_get.return_value.json.return_value = [{"price": 1}]

    assert get_share_price() == [
        {"stock": "AAPL", "price": 1},
        {"stock": "AMZN", "price": 1},
        {"stock": "GOOGL", "price": 1},
        {"stock": "MSFT", "price": 1},
        {"stock": "TSLA", "price": 1},
    ]


@patch("requests.request")
def test_get_exchange_rate(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 1}}

    assert get_exchange_rate() == [{"currency": "USD", "rate": 1}, {"currency": "EUR", "rate": 1}]
