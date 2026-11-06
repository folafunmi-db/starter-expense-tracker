from expense_tracker.commands import add, top
from expense_tracker.cli import build_parser
from tests.conftest import args, make_store


def _seed(store):
    add.handle(
        args(amount="12.50", category="groceries", date="2026-01-15", note="weekly shop"),
        store,
    )
    add.handle(
        args(amount="40.00", category="transport", date="2026-01-16", note=""),
        store,
    )
    add.handle(args(amount="5.00", category="coffee", date="2026-01-17", note=""), store)


def test_top_orders_largest_first_and_respects_limit(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()

    code = top.handle(args(limit=2), store)

    out = capsys.readouterr().out.splitlines()
    assert code == 0
    assert out == [
        "#2  2026-01-16      $40.00  transport",
        "#1  2026-01-15      $12.50  groceries  (weekly shop)",
    ]


def test_top_limit_larger_than_expense_count_prints_all(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()

    code = top.handle(args(limit=10), store)

    out = capsys.readouterr().out.splitlines()
    assert code == 0
    assert len(out) == 3
    assert [line.split()[2] for line in out] == ["$40.00", "$12.50", "$5.00"]


def test_top_limit_defaults_to_three():
    parsed = build_parser().parse_args(["top"])

    assert parsed.limit == 3