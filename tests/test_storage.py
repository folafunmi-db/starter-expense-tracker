from expense_tracker.models import Expense
from expense_tracker.storage import Store


def test_round_trip(tmp_path):
    store = Store(path=tmp_path / "expenses.json")
    store.save([Expense(id=1, amount_cents=999, category="misc", date="2026-02-02", note="x")])
    loaded = store.load()
    assert loaded == [Expense(id=1, amount_cents=999, category="misc", date="2026-02-02", note="x")]


def test_load_missing_file_is_empty(tmp_path):
    store = Store(path=tmp_path / "nope.json")
    assert store.load() == []


def test_next_id_on_empty(tmp_path):
    store = Store(path=tmp_path / "expenses.json")
    assert store.next_id([]) == 1
