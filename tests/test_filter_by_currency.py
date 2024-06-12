from src.generators import filter_by_currency


def test_filter_by_currency(transactions_coll):
    usd_transactions = filter_by_currency(transactions_coll, "USD")
    assert (next(usd_transactions)["id"]) == 939719570
    assert (next(usd_transactions)["id"]) == 142264268
