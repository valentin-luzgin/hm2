from src.masks import masked_account_number, masked_card_number


def masked_cards_and_accounts(splited_str: str) -> str:
    """Возвращает тип номера карты/счета и маскрированный номер"""
    masked_number = str()
    for i in splited_str.split():
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
