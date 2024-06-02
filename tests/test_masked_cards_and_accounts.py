import pytest
from src.widget import masked_cards_and_accounts


@pytest.mark.parametrize(
    "value, expected",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Счет 64686473678894779589", "Счет **9589")],
)
def test_masked_cards_and_accounts(value, expected):
    assert masked_cards_and_accounts(value) == expected
