def masked_cards_and_accounts(card_account_number: str) -> str | None:
    '''Возвращает маскированные номера карт и счетов'''
    splited_str = card_account_number.split()
    masked_number = str()
    for i in splited_str:
        if i.isalpha():
            masked_number += i + ' '
        elif i.isdigit() and len(i) == 16:
            masked_number += f"{i[:4]} {i[5:7]}{'**'} {'****'} {i[12:]}"
        elif i.isdigit() and len(i) == 20:
            masked_number += f"{'**'}{i[16:]}"
    return masked_number

