from src.widget import masked_cards_and_accounts, date_conversion


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
