def masked_card_number(card_number: str) -> str | None:
    """Возвращает маскированные номера карт."""
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[5:7]}{'**'} {'****'} {card_number[12:]}"
    else:
        return None


def masked_account_number(account_number: str) -> str | None:
    """Возвращает маскированные номера счетов."""
    if len(account_number) == 20:
        return f"{'**'}{account_number[16:]}"
    else:
        return None

