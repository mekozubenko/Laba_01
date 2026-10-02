
from unittest.mock import patch

import pytest

from toolkit.__main__ import main


def test_cli_calc_success():
    # Имитируем запуск: python -m toolkit calc "2+2"
    with patch('sys.argv', ['toolkit', 'calc', '2+2']):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0

def test_cli_convert_success():
    # Имитируем запуск: python -m toolkit convert 100 g --from g --to kg
    with patch('sys.argv', ['toolkit', 'convert', '100', '--from', 'g', '--to', 'kg']):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0

def test_cli_invalid_command():
    # Имитируем ввод несуществующей команды
    with patch('sys.argv', ['toolkit', 'unknown_command']):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 2