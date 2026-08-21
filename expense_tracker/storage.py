"""JSON-file persistence for expenses.

The data file location defaults to ``expenses.json`` in the current working
directory, and can be overridden with the ``EXPENSE_TRACKER_DATA``
environment variable (handy for tests and for keeping cohorts isolated).
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from .models import Expense

DEFAULT_FILENAME = "expenses.json"


def data_path() -> Path:
    """Return the path to the JSON data file."""
    override = os.environ.get("EXPENSE_TRACKER_DATA")
    return Path(override) if override else Path.cwd() / DEFAULT_FILENAME


class Store:
    """A thin load/save wrapper around the JSON data file."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or data_path()

    def load(self) -> list[Expense]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return [Expense.from_dict(item) for item in raw]

    def save(self, expenses: list[Expense]) -> None:
        payload = [e.to_dict() for e in expenses]
        self.path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def next_id(self, expenses: list[Expense]) -> int:
        return 1 + max((e.id for e in expenses), default=0)
