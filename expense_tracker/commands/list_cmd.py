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


def handle(args, store) -> int:
    expenses = store.load()
    if args.category is not None:
        expenses = [e for e in expenses if e.category == args.category]

    if not expenses:
        print("No expenses found.")
        return 0

    for e in expenses:
        note = f"  ({e.note})" if e.note else ""
        print(f"#{e.id}  {e.date}  {format_amount(e.amount_cents):>10}  {e.category}{note}")
    return 0
