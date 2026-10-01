from errors import ConversionError

units_of_measurument = {
    'distance': {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
    },
    'mass': {
        'g': 1.0,
        'kg': 1000.0,
    }
}
units_of_temperature = {'c', 'f', 'k'}

def convert (value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    try:
        value = float(value)
    except (ValueError, TypeError):
        raise ConversionError(f"Неверное числовое значение: '{value}'")
    if from_unit in units_of_temperature and to_unit in units_of_temperature:
        if from_unit == 'c':
            if value >= -273.15:
                if to_unit == 'c':
                    return value
                if to_unit == 'f':
                    return value * 9 / 5 + 32
                if to_unit == 'k':
                    return value + 273
            else:
                raise ConversionError('Температура ниже абсолютного нуля запрещена.')
        elif from_unit == 'f':
            if value >= -459.67:
                if to_unit == 'c':
                    return (value - 32) * 5 / 9
                if to_unit == 'f':
                    return value
                if to_unit == 'k':
                    return (value - 32) * 5 / 9 + 273
            else:
                raise ConversionError('Температура ниже абсолютного нуля запрещена.')
        elif from_unit == 'k':
            if value >= 0:
                if to_unit == 'c':
                    return value - 273
                if to_unit == 'k':
                    return value
                if to_unit == 'f':
                    return (value - 32) * 5 / 9 + 273
            else:
                raise ConversionError('Температура ниже абсолютного нуля запрещена.')
    elif from_unit in units_of_measurument['length'] and to_unit in units_of_measurument['length']:
        units = units_of_measurument['length']
        return (value * units[from_unit] / units[to_unit])
    elif from_unit in units_of_measurument['mass'] and to_unit in units_of_measurument['mass']:
        units = units_of_measurument['mass']
        return (value * units[from_unit] / units[to_unit])
    else:
        raise ConversionError('Несоответствие единиц измерения.')