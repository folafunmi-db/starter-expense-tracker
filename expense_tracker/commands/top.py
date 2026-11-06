"""The ``top`` command: show the largest expenses."""

from __future__ import annotations

from .list_cmd import format_expense

NAME = "top"
HELP = "Show the largest expenses"


def _positive_limit(value: str) -> int:
    limit = int(value)
    if limit < 1:
        raise ValueError("limit must be a positive integer")
    return limit


def add_parser(subparsers) -> None:
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument(
        "--limit",
        type=_positive_limit,
        default=3,
        metavar="N",
        help="Number of expenses to show (default: 3)",
    )


def handle(args, store) -> int:
    expenses = sorted(
        store.load(),
        key=lambda expense: expense.amount_cents,
        reverse=True,
    )[: args.limit]

    if not expenses:
        print("No expenses found.")
        return 0

    for expense in expenses:
        print(format_expense(expense))
    return 0