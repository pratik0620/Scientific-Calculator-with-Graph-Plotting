import numpy as np
import math
import re

def add(num1, num2):
    return np.add(num1, num2)

def sub(num1, num2):
    return np.subtract(num1, num2)

def mul(num1, num2):
    return np.multiply(num1, num2)

def div(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero")
    return np.divide(num1, num2)

def power(num1, num2):
    return np.power(num1, num2)

def sqrt(num):
    return np.sqrt(num)

def log(num):
    return np.log10(num)

def ln(num):
    return np.log(num)

def sin(num):
    return np.sin(np.radians(num))

def cos(num):
    return np.cos(np.radians(num))

def tan(num):
    return np.tan(np.radians(num))

def factorial(num):
    if num < 0:
        raise ValueError("Factorial of negative number")
    return math.factorial(int(num))

def reciprocal(num):
    if num == 0:
        raise ValueError("Division by zero")
    return 1 / num

def percentage(num):
    return num / 100

def evaluate_expression(expr):

    expr = re.sub(r'(\d+)!', r'factorial(\1)', expr)
    expr = expr.replace('%', '/100')
    expr = expr.replace('^', '**')
    expr = expr.replace('÷', '/')
    expr = expr.replace('×', '*')
    expr = expr.replace('π', 'pi')
    allowed_names = {
        'sin': sin,
        'cos': cos,
        'tan': tan,
        'log': log,
        'ln': ln,
        'sqrt': sqrt,
        'factorial': factorial,
        'reciprocal': reciprocal,
        'percentage': percentage,
        'pi': np.pi,
        'e': np.e,
        'pow': power,
    }

    try:
        result = eval(expr, {"__builtins__": None}, allowed_names)
    except Exception as e:
        raise e
    return result
