import json


def operations_to_list_of_dicts(path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    list_of_dicts = []
    try:
        with open(path) as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    for i in data:
                        list_of_dicts.append(i)
                    return list_of_dicts
                else:
                    return list_of_dicts
            except json.JSONDecodeError:
                return list_of_dicts
    except FileNotFoundError:
        return list_of_dicts
