"""The ``list`` command: show recorded expenses."""

from __future__ import annotations

from ..money import format_amount

NAME = "list"
HELP = "List expenses, optionally filtered by category"


def add_parser(subparsers) -> None:
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument(
        "--category",
        default=None,
        help="Only show expenses in this category",
    )


def format_expense(expense) -> str:
    note = f"  ({expense.note})" if expense.note else ""
    return (
        f"#{expense.id}  {expense.date}  "
        f"{format_amount(expense.amount_cents):>10}  "
        f"{expense.category}{note}"
    )


def handle(args, store) -> int:
    expenses = store.load()
    if args.category is not None:
        expenses = [e for e in expenses if e.category == args.category]

    if not expenses:
        print("No expenses found.")
        return 0

    for expense in expenses:
        print(format_expense(expense))
    return 0
