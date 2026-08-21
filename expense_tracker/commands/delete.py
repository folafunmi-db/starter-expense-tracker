"""The ``delete`` command: remove an expense by id."""

from __future__ import annotations

NAME = "delete"
HELP = "Delete an expense by its id"


def add_parser(subparsers) -> None:
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument("id", type=int, help="The id of the expense to delete")


def handle(args, store) -> int:
    expenses = store.load()
    remaining = [e for e in expenses if e.id != args.id]

    if len(remaining) == len(expenses):
        print(f"error: no expense with id {args.id}")
        return 1

    store.save(remaining)
    print(f"Deleted #{args.id}")
    return 0
