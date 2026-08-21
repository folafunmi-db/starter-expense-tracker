"""Command-line entry point.

Builds the argument parser from the command registry and dispatches to the
matching command's ``handle`` function.
"""

from __future__ import annotations

import argparse
import sys

from . import __version__
from .commands import COMMANDS
from .storage import Store


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="A small command-line expense tracker.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command", metavar="<command>")
    subparsers.required = True

    for module in COMMANDS:
        module.add_parser(subparsers)

    return parser


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    args = parser.parse_args(argv)

    store = Store()
    for module in COMMANDS:
        if module.NAME == args.command:
            return module.handle(args, store)

    parser.error(f"unknown command: {args.command}")
    return 2  # unreachable; parser.error exits


if __name__ == "__main__":
    raise SystemExit(main())
