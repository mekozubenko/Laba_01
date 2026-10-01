from errors import DivisionByZero, ValidationError
def tokenize(expression):
    s = expression.replace(' ', '')
    tokens = []
    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit() or char == '.':
            number = ''
            while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                number += s[i]
                i += 1
            tokens.append(number)
            continue
        elif char in '()':
            tokens.append(char)
            i += 1
            continue
        elif char in '+-*/':
            if char in '+-' and (i == 0 or s[i-1] in '+-*/'):
                number = char
                i += 1
                while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                    number += s[i]
                    i += 1
                tokens.append(number)
                continue
            else:
                tokens.append(char)
                i += 1
                continue
        else:
            raise ValidationError(f'Недопустимый символ в выражении: {char}')

    return tokens

def validate(expression):
    tokens = tokenize(expression)
    if not tokens:
        raise ValidationError("Выражение не может быть пустым")
    allowed_chars = '+-*/()'
    binary_operators = ['+', '-', '*', '/']
    for token in tokens:
        is_number = token.replace('.', '', 1).replace('-', '', 1).isdigit()
        is_operation = token in allowed_chars
        if not (is_number or is_operation):
            raise ValidationError(f'Недопустимый символ или формат числа: {token}')
    if tokens[0] in binary_operators or tokens[-1] in binary_operators:
        raise ValidationError('Выражение не может начинаться или заканчиваться знаком операции.')
    brackets_count = 0
    for i in range(len(tokens)):
        current = tokens[i]
        if current == '(':
            brackets_count += 1
            if i + 1 < len(tokens) and tokens[i+1] == ')':
                raise ValidationError('Обнаружены пустые скобки')
        elif current == ')':
            brackets_count -= 1
            if brackets_count < 0:
                raise ValidationError('Нарушен баланс скобок, закрывающая идет раньше открывающей')
        elif current in binary_operators:
            next_token = tokens[i+1] if i + 1 < len(tokens) else None
            if next_token in binary_operators:
                raise ValidationError(f'Два знака операции стоят рядом: {current} и {next_token}')
            if next_token == ')':
                raise ValidationError('Знак операции не может стоять перед закрывающей скобкой')
    if brackets_count != 0:
        raise ValidationError('Нарушен баланс скобок')
    return True

def to_polish_notation(tokens):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    output_string = [] #то, что сразу выносится на экран
    stack = [] #стек, в который кладем знаки операций и скобки
    for token in tokens:
        if token not in '+-*/' and token not in '()':
            output_string.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output_string.append(stack.pop())
            stack.pop()
        elif token in '+-*/':
            while (stack and stack[-1] in '+-*/' and priority[stack[-1]] >= priority[token]):
                output_string.append(stack.pop())
            stack.append(token)
    while stack:
        op = stack.pop()
        output_string.append(op)
    return output_string

def calculate(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if token in '+-*/':
            if len(stack) < 2:
                raise ValidationError('Недостаточно операндов для выполнения операции')
            b = stack.pop()
            a = stack.pop()
            #операнды, над которыми будем производить действия. сначала правый, потом левый
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise DivisionByZero('Деление на ноль запрещено!')
                result = a / b
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValidationError(f'Невозможно проебразовать токен {token} в число.')
    if len(stack) != 1:
        raise ValidationError('Выражение содержит лишние операнды.')
    return stack[0]