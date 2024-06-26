from unittest.mock import patch

from src.external_api import get_transaction_amount_in_rubles


@patch("requests.get")
def test_get_transaction_amount_in_rubles_usd(mock_get):
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "100.00", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8725}
    assert get_transaction_amount_in_rubles(transaction) == 8725


@patch("requests.get")
def test_get_transaction_amount_in_rubles_rub(mock_get):
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "100.00", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_transaction_amount_in_rubles(transaction) == 100
