"""Shared test helpers."""

from __future__ import annotations

import argparse

from expense_tracker.storage import Store


def make_store(tmp_path) -> Store:
    return Store(path=tmp_path / "expenses.json")


def args(**kwargs) -> argparse.Namespace:
    return argparse.Namespace(**kwargs)
