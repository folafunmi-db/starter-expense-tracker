"""Money handling.

Amounts are stored and passed around as an integer number of minor units
(cents). Never use floats for money: float arithmetic loses precision and
will eventually produce wrong totals.
"""

from __future__ import annotations


class MoneyError(ValueError):
    """Raised when a money string cannot be parsed into whole cents."""


def parse_amount(raw: str) -> int:
    """Parse a user-supplied amount like "12.50" or "12" into integer cents.

    Rejects negative values, blanks, and inputs with more than two decimal
    places rather than silently rounding them.
    """
    text = (raw or "").strip()
    if not text:
        raise MoneyError("amount is required")
    if text.startswith("-"):
        raise MoneyError("amount must not be negative")

    if "." in text:
        whole, _, frac = text.partition(".")
    else:
        whole, frac = text, ""

    if not whole.isdigit() or (frac and not frac.isdigit()):
        raise MoneyError(f"not a valid amount: {raw!r}")
    if len(frac) > 2:
        raise MoneyError(f"amount has more than two decimal places: {raw!r}")

    cents = int(whole) * 100 + int((frac + "00")[:2])
    return cents


def format_amount(cents: int) -> str:
    """Render integer cents as a display string like "$12.50".

    Uses integer arithmetic only, so the displayed value can never drift.
    """
    dollars, remainder = divmod(cents, 100)
    return f"${dollars}.{remainder:02d}"
