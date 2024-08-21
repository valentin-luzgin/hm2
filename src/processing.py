import re
from collections import Counter


def return_dict_containing_key_passed_to_function(list_of_states: list, state: str = "EXECUTED") -> list:
    """возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию
    значение."""
    new_list = []
    for i in list_of_states:
        if i.get("state") == state:
            new_list.append(i)
    return new_list


def sort_dicts_by_date(data: list, reverse: bool = True) -> list:
    """возвращает отсортированный по времени список"""
    operations = sorted(data, key=lambda x: x.get("date"), reverse=reverse)
    return operations


def search_in_list_of_transaction_dictionaries(transactions: list, user_input: str) -> list:
    """возвращает список словарей с транзакциями, в описании которых содержится переданное пользователем значение"""
    new_list = []
    for i in transactions:
        if re.search(user_input, i.get("description"), flags=re.IGNORECASE):
            new_list.append(i)
    return new_list


def description_type_count(transactions: list) -> Counter:
    """принимает список словарей с данными о банковских операциях и возвращает словарь с названиями категорий и их
    количеством"""
    description_type = []
    for transaction in transactions:
        description_type.append(transaction.get("description"))
    return Counter(description_type)
