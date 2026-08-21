from expense_tracker.commands import add, list_cmd
from tests.conftest import args, make_store


def _seed(store):
    add.handle(args(amount="10.00", category="food", date="2026-01-01", note=""), store)
    add.handle(args(amount="20.00", category="travel", date="2026-01-02", note=""), store)
    add.handle(args(amount="5.00", category="food", date="2026-01-03", note=""), store)


def test_list_all(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()  # discard output from seeding
    code = list_cmd.handle(args(category=None), store)
    out = capsys.readouterr().out
    assert code == 0
    assert out.count("\n") == 3


def test_list_filtered_by_category(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()  # discard output from seeding
    list_cmd.handle(args(category="food"), store)
    out = capsys.readouterr().out
    assert "food" in out
    assert "travel" not in out


def test_list_empty(tmp_path, capsys):
    store = make_store(tmp_path)
    code = list_cmd.handle(args(category=None), store)
    out = capsys.readouterr().out
    assert code == 0
    assert "No expenses found." in out
