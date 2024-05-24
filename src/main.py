from src.widget import masked_cards_and_accounts, date_conversion
from src.processing import return_dict_containing_key_passed_to_function, sort_dicts_by_date

bank_list = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]


for i in bank_list:
    print(masked_cards_and_accounts(i))


print(date_conversion("2018-07-11T02:26:18.671407"))


list_of_states = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(return_dict_containing_key_passed_to_function(list_of_states, state="EXECUTED"))
print(sort_dicts_by_date(list_of_states, reverse=False))
