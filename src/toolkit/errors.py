class ToolkitError(Exception):
    pass
class DivisionByZero(ToolkitError):
    pass
#деление на ноль
class ValidationError(ToolkitError):
    pass
#ошибка валидации
class ConversionError(ToolkitError):
    pass
#ошибка конвертера