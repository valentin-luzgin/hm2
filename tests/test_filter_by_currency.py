from src.generators import filter_by_currency
from src.main import transactions


def test_filter_by_currency():
    usd_transactions = filter_by_currency(transactions, "USD")
    assert (next(usd_transactions)["id"]) == 939719570
    assert (next(usd_transactions)["id"]) == 142264268
