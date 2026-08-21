"""The ``add`` command: record a new expense."""

from __future__ import annotations

from datetime import date as date_cls

from ..models import Expense
from ..money import MoneyError, format_amount, parse_amount

NAME = "add"
HELP = "Add a new expense"


def add_parser(subparsers) -> None:
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument("amount", help="Amount, e.g. 12.50")
    parser.add_argument("category", help="Category, e.g. groceries")
    parser.add_argument("date", help="Date in YYYY-MM-DD format")
    parser.add_argument("--note", default="", help="Optional free-text note")


def _validate_date(value: str) -> str:
    # Raises ValueError on a malformed date; the CLI turns that into an error.
    date_cls.fromisoformat(value)
    return value


def handle(args, store) -> int:
    try:
        amount_cents = parse_amount(args.amount)
        iso_date = _validate_date(args.date)
    except (MoneyError, ValueError) as exc:
        print(f"error: {exc}")
        return 1

    expenses = store.load()
    expense = Expense(
        id=store.next_id(expenses),
        amount_cents=amount_cents,
        category=args.category,
        date=iso_date,
        note=args.note,
    )
    expenses.append(expense)
    store.save(expenses)
    print(
        f"Added #{expense.id}: {format_amount(amount_cents)} "
        f"{expense.category} on {expense.date}"
    )
    return 0
