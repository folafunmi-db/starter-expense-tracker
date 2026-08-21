import pytest

from expense_tracker.money import MoneyError, format_amount, parse_amount


def test_parse_whole_number():
    assert parse_amount("12") == 1200


def test_parse_two_decimals():
    assert parse_amount("12.50") == 1250


def test_parse_one_decimal():
    assert parse_amount("12.5") == 1250


def test_parse_strips_whitespace():
    assert parse_amount("  7.05  ") == 705


def test_parse_rejects_blank():
    with pytest.raises(MoneyError):
        parse_amount("")


def test_parse_rejects_negative():
    with pytest.raises(MoneyError):
        parse_amount("-3.00")


def test_parse_rejects_three_decimals():
    with pytest.raises(MoneyError):
        parse_amount("1.234")


def test_parse_rejects_non_numeric():
    with pytest.raises(MoneyError):
        parse_amount("ten")


def test_format_pads_cents():
    assert format_amount(705) == "$7.05"


def test_format_whole():
    assert format_amount(1200) == "$12.00"
