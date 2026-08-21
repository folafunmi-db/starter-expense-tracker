from expense_tracker.commands import add, delete
from tests.conftest import args, make_store


def test_delete_removes_expense(tmp_path):
    store = make_store(tmp_path)
    add.handle(args(amount="10.00", category="food", date="2026-01-01", note=""), store)
    code = delete.handle(args(id=1), store)
    assert code == 0
    assert store.load() == []


def test_delete_unknown_id_errors(tmp_path):
    store = make_store(tmp_path)
    add.handle(args(amount="10.00", category="food", date="2026-01-01", note=""), store)
    code = delete.handle(args(id=99), store)
    assert code == 1
    assert len(store.load()) == 1
