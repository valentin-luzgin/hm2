import pytest

from src.main import my_function


@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9)])
def test_my_function(capsys, x, y, expected):
    my_function(x, y)
    captured = capsys.readouterr()
    assert captured.out == f"{expected}\n"
