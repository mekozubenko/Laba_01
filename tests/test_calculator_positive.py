import pytest

from toolkit.calculator import calculate
from toolkit.calculator import to_polish_notation
from toolkit.calculator import tokenize
from toolkit.calculator import validate


def run_calc(expression):
    """Отдельная функция, чтобы каждый раз не дублировать вызов функции."""
    validate(expression)
    tokens = tokenize(expression)
    postfix = to_polish_notation(tokens)
    return calculate(postfix)

def test_basic_ops():
    assert run_calc('5 + 5') == 10.0
    assert run_calc('10 - 2') == 8.0
    assert run_calc('7 * 3') == 21.0
    assert run_calc('64 / 8') == 8.0

def test_operator_priority():
    assert run_calc('2 + 3 * 4') == 14.0
    assert run_calc('2 * 3 + 4') == 10.0
    assert run_calc('10 - 6 / 2') == 7.0

def test_brackets():
    assert run_calc('(5 + 3) * 4') == 32.0
    assert run_calc('24 / (2 * ( 5 - 2 ))') == 4.0

def test_float_nums():
    assert run_calc('2.5 + 3.1') == pytest.approx(5.6)
    assert run_calc('10 / 4') == pytest.approx(2.5)
    assert run_calc('0.1 * 0.2') == pytest.approx(0.02)

def test_unary_operators():
    assert run_calc('-5 + 3') == -2.0
    assert run_calc('5 * -3') == -15.0
    assert run_calc('2 * 3 * 5 * (-5)') == -150.0
    assert run_calc(' +5 + 3') == 8.0
    assert run_calc('5 * + 3') == 15.0

def test_spaces():
    assert run_calc('  2  +  3  *  4  ') == 14.0
    assert run_calc('  (  - 5.5  / 2  )  ') == pytest.approx(-2.75)
