import pytest

from toolkit.calculator import calculate
from toolkit.calculator import to_polish_notation
from toolkit.calculator import tokenize
from toolkit.calculator import validate
from toolkit.errors import DivisionByZero
from toolkit.errors import ValidationError


def test_empty_expression():
    with pytest.raises(ValidationError):
        calculate("")

def test_invalid_characters():
    with pytest.raises(ValidationError):
        calculate("5 & 3")

def test_two_binary_operators():
    with pytest.raises(ValidationError):
        calculate("5 ++ 3")

def test_division_by_zero():
    with pytest.raises(DivisionByZero):
        validate("5 / 0")
        tokens = tokenize("5 / 0")
        postfix = to_polish_notation(tokens)
        calculate(postfix)

def test_invalid_numeric_value():
    with pytest.raises(ValidationError):
        calculate("a + b")