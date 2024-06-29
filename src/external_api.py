import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data["result"])
    else:
        raise ValueError(f"Неизвестная валюта {currency}.")
