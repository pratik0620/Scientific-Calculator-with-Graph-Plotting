import numpy as np
import matplotlib.pyplot as plt
import math

def plot_equation(equation_str):

    equation_str = equation_str.replace('^', '**')
    equation_str = equation_str.replace('÷', '/')
    equation_str = equation_str.replace('×', '*')
    equation_str = equation_str.replace('π', str(math.pi))
    equation_str = equation_str.replace('e', str(math.e))

    # Define a safe list of functions for eval
    allowed_funcs = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'log': np.log10,
        'ln': np.log,
        'sqrt': np.sqrt,
        'abs': np.abs,
        'pi': math.pi,
        'e': math.e,
        'exp': np.exp,
        'pow': pow,
    }

    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Define a function to evaluate y for each x
    def eval_func(x_val):
        try:
            # Use eval with allowed functions and x value
            return eval(equation_str, {"__builtins__": None, **allowed_funcs, 'x': x_val})
        except Exception:
            return np.nan

    y = np.vectorize(eval_func)(x)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {equation_str}')
    plt.title('Graph of the equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
