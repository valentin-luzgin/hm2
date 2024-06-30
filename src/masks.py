import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/log.log",
    filemode="w",
)

masks_logger = logging.getLogger("app.masks")


def masked_card_number(card_number: str) -> str:
    """Возвращает маскированные номера карт."""
    masks_logger.info("Замаскирован номер карты")
    return f"{card_number[:4]} {card_number[4:6]}{'**'} {'****'} {card_number[12:]}"


def masked_account_number(account_number: str) -> str:
    """Возвращает маскированные номера счетов."""
    masks_logger.info("Замаскирован номер счета")
    return f"{'**'}{account_number[16:]}"
