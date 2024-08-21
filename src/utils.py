import csv
import json
import logging

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/log.log",
    filemode="w",
)

utils_logger = logging.getLogger("app.utils")


def operations_to_list_of_dicts(path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    list_of_dicts = []
    try:
        with open(path) as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    for i in data:
                        if i == {}:
                            continue
                        else:
                            utils_logger.info("Добавлен словарь")
                            list_of_dicts.append(i)
                    return list_of_dicts
                else:
                    utils_logger.warning("JSON-файл не найден")
                    return list_of_dicts
            except json.JSONDecodeError:
                utils_logger.warning("Ошибка декодирования")
                return list_of_dicts
    except FileNotFoundError:
        utils_logger.warning("Файл не найден")
        return list_of_dicts


def csv_to_list_of_dicts(file: str) -> list[dict]:
    """принимает на вход путь до CVS-файла и возвращает список словарей с данными о финансовых транзакциях"""
    with open(file) as file:
        list_of_dicts = []
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        for row in reader:
            row_dict = dict()
            for idx, item in enumerate(header):
                row_dict[item] = row[idx]
            list_of_dicts.append(row_dict)
    return list_of_dicts


def xlsx_to_list_of_dicts(file: str) -> list[dict]:
    """принимает на вход путь до xlsx-файла и возвращает список словарей с данными о финансовых транзакциях"""
    list_of_dicts = []
    df = pd.read_excel(file)
    for index, row in df.iterrows():
        if not all(row.isnull()):
            list_of_dicts.append(row.to_dict())
    return list_of_dicts
