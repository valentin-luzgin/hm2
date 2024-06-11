import pytest

from src.widget import date_conversion


@pytest.mark.parametrize("value, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_date_conversion(value, expected):
    assert date_conversion(value) == expected
