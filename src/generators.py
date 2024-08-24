import re
from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[list, int, None]:
    """сортирует операции по переданному в функцию коду валюты"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            if transaction.get("currency_code") == currency:
                yield transaction


def transaction_descriptions(transactions: list) -> Generator[str, str, None]:
    """выводит описание транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Generator[str, str, None]:
    """генерирует номера карт в заданном диапозоне"""
    while start <= end:
        generated_card_number = f"{start:0>16}"
        cp = re.match(r"(\d*)(\d{4})(\d{4})(\d{4})", generated_card_number)
        yield cp[1] + " " + cp[2] + " " + cp[3] + " " + cp[4]
        start += 1
