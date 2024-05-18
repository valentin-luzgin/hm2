def masked_card_number(card_number: str) -> str:
    """Возвращает маскированные номера карт."""
    return f"{card_number[:4]} {card_number[5:7]}{'**'} {'****'} {card_number[12:]}"


def masked_account_number(account_number: str) -> str:
    """Возвращает маскированные номера счетов."""
    return f"{'**'}{account_number[16:]}"
