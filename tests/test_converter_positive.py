from toolkit.converter import convert


def test_length_conversion():
    assert convert("1", "m", "cm") == 100.0
    assert convert("500", "mm", "m") == 0.5
    assert convert("2.5", "km", "m") == 2500.0


def test_mass_conversion():
    assert convert("1", "kg", "g") == 1000.0
    assert convert("250", "g", "kg") == 0.25


def test_temperature_conversion():
    assert convert("0", "c", "k") == 273.15
    assert convert("100", "c", "f") == 212.0
    assert convert("32", "f", "c") == 0.0


def test_case_insensitivity():
    assert convert("1", "M", "CM") == 100.0
    assert convert("1000", "g", "KG") == 1.0
    assert convert("0", "C", "k") == 273.15
