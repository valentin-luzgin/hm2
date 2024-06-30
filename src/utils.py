import json
import logging

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
