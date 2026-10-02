import pytest

from toolkit.converter import convert
from toolkit.errors import ConversionError


def test_error_unknown_unit():
    with pytest.raises(ConversionError):
        # Единица 'mile' не поддерживается тулкитом
        convert("10", "m", "mile")

    with pytest.raises(ConversionError):
        convert("5", "xyz", "kg")


def test_error_incompatible_units():
    with pytest.raises(ConversionError):
        convert("10", "m", "kg")

    with pytest.raises(ConversionError):
        convert("100", "g", "c")


def test_error_absolute_zero():
    with pytest.raises(ConversionError):
        convert("-274", "c", "k")

    with pytest.raises(ConversionError):
        convert("-1", "k", "c")


def test_error_invalid_numeric_value():
    """Тест: ошибка, если вместо числа передана некорректная строка."""
    with pytest.raises(ConversionError):
        convert("abc", "m", "cm")

    with pytest.raises(ConversionError):
        convert("12.3.4", "kg", "g")
