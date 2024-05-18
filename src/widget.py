from typing import Union
from src.masks import masked_card_number, masked_account_number

splited_str = []


def splits_string_into_type_and_number(card_account_number: str) -> list:
    """Разделяет строку на тип карты/счета и номер"""
    global splited_str
    splited_str = card_account_number.split()
    return splited_str


def masked_cards_and_accounts(splited_str: Union[list]) -> Union[str]:
    """Возвращает тип номера карты/счета и маскрированный номер"""
    masked_number = str()
    for i in splited_str:
        if i.isalpha():
            masked_number += i + " "
        elif i.isdigit() and len(i) == 16:
            masked_number += masked_card_number(i)
        elif i.isdigit() and len(i) == 20:
            masked_number += masked_account_number(i)
    return masked_number


def date_conversion(date: str) -> str:
    """Преобразует дату формата ГГГГ-ММ-ДД в формат ДД-ММ-ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


splits_string_into_type_and_number("Visa Classic 6831982476737658")
