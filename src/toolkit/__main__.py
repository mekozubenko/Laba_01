import sys

from toolkit.calculator import calculate
from toolkit.calculator import to_polish_notation
from toolkit.calculator import tokenize
from toolkit.calculator import validate
from toolkit.converter import convert
from toolkit.errors import ToolkitError
from toolkit.errors import ValidationError


def print_help():
    """Выводит справку об использовании консольного набора утилит."""
    help_text = (
        "Использование консольного набора утилит:\n"
        "   python -m toolkit calc \'EXPRESSION\'                         - Вычисление значения математического выражения.\n"
        "   python -m toolkit convert VALUE --from UNIT --to UNIT       - Конвертация величины из одной единицы измерения в другую.\n" 
        "   python -m toolkit --help                                    - Показать справку."
    )
    print(help_text)

def main():
    """Вычислительное ядро калькулятора. Разбирает аргументы из командной строки и вызывает нужные функции в зависимости от команды."""
    args = sys.argv[1:]
    if not args or '--help' in args or '--h' in args:
        print_help()
        sys.exit(0)
    command = args[0]
    try:
        if command == 'calc':
            if len(args) != 2:
                raise ValidationError('Калькулятор принимает ровно один аргумент: выражение в кавычках.')
            expression = args[1]
            validate(expression)
            tokens = tokenize(expression)
            postfix = to_polish_notation(tokens)
            result = calculate(postfix)

            print(result)
            sys.exit(0)
        elif command == 'convert':
            if len(args) != 6:
                raise ValidationError('Неверный формат команды convert, ожидается: convert VALUE --from UNIT --to UNIT.')
            value = args[1]
            try:
                from_idx = args.index('--from')
                to_idx = args.index('--to')
            except ValueError:
                raise ValidationError('Команда convert должна содержать и единицы измерени, из которых вы переводите, и те, в которые нужно перевести.')
            if from_idx + 1 >= len(args) or to_idx + 1 >= len(args):
                raise ValidationError('Не указано значение для величин для перевода.')
            from_unit = args[from_idx + 1]
            to_unit = args[to_idx + 1]

            result = convert(value, from_unit, to_unit)
            print(result)
            sys.exit(0)
        else:
            raise ValidationError(f'Неизвесьная команда: {command}')
    except ToolkitError as e:
        print(f'Ошибка: {e}', file = sys.stderr)
        sys.exit(2)
    except Exception as e: # noqa: BLE001
        print(f'Критическая ошибка {e}', file = sys.stderr)
        sys.exit(2)
if __name__ == "__main__":
    main()