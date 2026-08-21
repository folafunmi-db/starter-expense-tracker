from expense_tracker.commands import add
from tests.conftest import args, make_store


def test_add_records_expense(tmp_path):
    store = make_store(tmp_path)
    code = add.handle(
        args(amount="12.50", category="groceries", date="2026-01-15", note=""),
        store,
    )
    assert code == 0
    saved = store.load()
    assert len(saved) == 1
    assert saved[0].amount_cents == 1250
    assert saved[0].category == "groceries"
    assert saved[0].date == "2026-01-15"


def test_add_assigns_incrementing_ids(tmp_path):
    store = make_store(tmp_path)
    add.handle(args(amount="1", category="a", date="2026-01-01", note=""), store)
    add.handle(args(amount="2", category="b", date="2026-01-02", note=""), store)
    saved = store.load()
    assert [e.id for e in saved] == [1, 2]


def test_add_rejects_bad_amount(tmp_path):
    store = make_store(tmp_path)
    code = add.handle(
        args(amount="lots", category="groceries", date="2026-01-15", note=""),
        store,
    )
    assert code == 1
    assert store.load() == []


def test_add_rejects_bad_date(tmp_path):
    store = make_store(tmp_path)
    code = add.handle(
        args(amount="5.00", category="groceries", date="15-01-2026", note=""),
        store,
    )
    assert code == 1
    assert store.load() == []
