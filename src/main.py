from src.generators import filter_by_currency
from src.processing import (return_dict_containing_key_passed_to_function, search_in_list_of_transaction_dictionaries,
                            sort_dicts_by_date)
from src.utils import csv_to_list_of_dicts, operations_to_list_of_dicts, xlsx_to_list_of_dicts
from src.widget import date_conversion, masked_cards_and_accounts


def main() -> None:
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    while True:
        print(
            "Привет! Добро пожаловать в программу работы  с банковскими транзакциями. Выберите необходимый "
            "пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из"
            " CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла"
        )
        type_file_choice = input().strip()
        if type_file_choice == "1":
            print("Для обработки выбран JSON-файл.")
            list_of_transactions_file = operations_to_list_of_dicts("../data/operations.json")
            break
        elif type_file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            list_of_transactions_file = csv_to_list_of_dicts("../data/transactions.csv")
            break
        elif type_file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            list_of_transactions_file = xlsx_to_list_of_dicts("../data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный ввод. Попробуй еще раз.")
            continue

    list_of_transactions = dict()
    while True:
        transaction_state_choice = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if transaction_state_choice in ["CANCELED", "PENDING", "EXECUTED"]:
            list_of_transactions["state"] = transaction_state_choice
            print(f"Операции отфильтрованы по статусу {transaction_state_choice}")
            break
        else:
            print(f'Статус операции "{transaction_state_choice}" недоступен.')
            continue
    while True:
        sort_by_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_by_date == "да":
            while True:
                sort_type = input("Отсортировать по возрастанию или по убыванию?\n").lower()
                if sort_type == "по возрастанию":
                    list_of_transactions["date"] = False
                    break
                if sort_type == "по убыванию":
                    list_of_transactions["date"] = True
                    break
                else:
                    print("Некорректный ввод. Попробуй еще раз.")
                    continue
            break
        elif sort_by_date == "нет":
            break
        else:
            print("Некорректный ввод. Попробуй еще раз.")
            continue
    while True:
        sort_currency = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if sort_currency == "да":
            list_of_transactions["currency"] = "RUB"
            break
        elif sort_currency == "нет":
            break
        else:
            print("Некорректный ввод. Попробуй еще раз.")
            continue
    while True:
        sort_key = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if sort_key == "да":
            key_word = input("Введите слово для поиска\n")
            list_of_transactions["description"] = key_word
            break
        elif sort_key == "нет":
            break
        else:
            print("Некорректный ввод. Попробуй еще раз.")
            continue

    for filter_type, filter_value in list_of_transactions.items():
        if filter_type == transaction_state_choice:
            transactions_state = return_dict_containing_key_passed_to_function(list_of_transactions_file, filter_value)
        else:
            transactions_state = list_of_transactions_file
        if filter_type == "date":
            transactions_date = sort_dicts_by_date(transactions_state, filter_value)
        else:
            transactions_date = transactions_state
        if filter_type == "currency":
            transactions_currency = filter_by_currency(transactions_date, filter_value)
        else:
            transactions_currency = transactions_date
        if filter_type == "description":
            final_list_of_transactions = search_in_list_of_transaction_dictionaries(
                transactions_currency, filter_value
            )
        else:
            final_list_of_transactions = transactions_currency

    if not final_list_of_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(final_list_of_transactions)}\n")
        for i in final_list_of_transactions:
            if i["description"] == "Открытие вклада":
                print(f"{date_conversion(i['date'])} {i['description']}")
                print(f"{masked_cards_and_accounts(i['to'])}")
                print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
            else:
                print(f"{date_conversion(i['date'])} {i['description']}")
                print(f"{masked_cards_and_accounts(i['from'])} -> {masked_cards_and_accounts(i['to'])}")
                print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


if __name__ == "__main__":
    main()
