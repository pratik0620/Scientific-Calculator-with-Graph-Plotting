import tkinter
from tkinter import *
import functions
from graph import plot_equation

FONT = ("Arial", 14, "bold")

# Color Palette
BG_COLOR = "#1e1e1e"
ENTRY_BG = "#2e2e2e"
ENTRY_FG = "#ffffff"
BTN_COLOR_NUM = "#3c3f41"
BTN_COLOR_OP = "#f39c12"
BTN_COLOR_FUNC = "#3498db"
BTN_COLOR_CTRL = "#e74c3c"
BTN_COLOR_EQ = "#2ecc71"
BTN_HOVER = "#555"

class CalculatorButton():

    def __init__(self, master, text, row, col, colspan=1, width=5, height=2, command=None, bg=BTN_COLOR_NUM):
        self.button = Button(master,
                             text=text,
                             width=width,
                             height=height,
                             font=FONT,
                             bg=bg,
                             fg="white",
                             activebackground=BTN_HOVER,
                             relief="flat",
                             command=command)
        self.button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

class CalculatorUI():

    def __init__(self):
        self.window = Tk()
        self.window.title("Scientific Calculator")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.expression = ""
        self.input_text = tkinter.StringVar()

        self.create_ui()

    def create_ui(self):

        title = Label(text="Scientific Calculator", font=("Arial", 18, "bold"), bg=BG_COLOR, fg="white")
        title.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        display_eq = Entry(font=("Arial", 18), width=25, bg=ENTRY_BG, fg=ENTRY_FG,
                           insertbackground="white", borderwidth=3, relief="sunken",
                           justify="right", textvariable=self.input_text)
        display_eq.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Row 1
        CalculatorButton(self.window, "AC", 2, 0, bg=BTN_COLOR_CTRL, command=self.clear)
        CalculatorButton(self.window, "DEL", 2, 1, bg=BTN_COLOR_CTRL, command=self.delete)
        CalculatorButton(self.window, "(", 2, 2, bg=BTN_COLOR_OP, command=lambda: self.append_number("("))
        CalculatorButton(self.window, ")", 2, 3, bg=BTN_COLOR_OP, command=lambda: self.append_number(")"))

        # Row 2
        CalculatorButton(self.window, "sin", 3, 0, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("sin"))
        CalculatorButton(self.window, "cos", 3, 1, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("cos"))
        CalculatorButton(self.window, "tan", 3, 2, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("tan"))
        CalculatorButton(self.window, "^", 3, 3, bg=BTN_COLOR_OP, command=lambda: self.append_operator("^"))

        # Row 3
        CalculatorButton(self.window, "log", 4, 0, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("log"))
        CalculatorButton(self.window, "ln", 4, 1, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("ln"))
        CalculatorButton(self.window, "x²", 4, 2, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("x²"))
        CalculatorButton(self.window, "√", 4, 3, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("sqrt"))

        # Row 4
        CalculatorButton(self.window, "π", 5, 0, bg=BTN_COLOR_FUNC, command=lambda: self.append_number("π"))
        CalculatorButton(self.window, "e", 5, 1, bg=BTN_COLOR_FUNC, command=lambda: self.append_number("e"))
        CalculatorButton(self.window, "1/x", 5, 2, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("1/"))
        CalculatorButton(self.window, "x!", 5, 3, bg=BTN_COLOR_FUNC, command=lambda: self.append_function("!"))

        # Row 5
        CalculatorButton(self.window, "x", 6, 0, command=lambda: self.append_number("x"))
        CalculatorButton(self.window, "y", 6, 1, command=lambda: self.append_number("y"))
        CalculatorButton(self.window, "%", 6, 2, bg=BTN_COLOR_OP, command=lambda: self.append_operator("%"))
        CalculatorButton(self.window, "÷", 6, 3, bg=BTN_COLOR_OP, command=lambda: self.append_operator("÷"))

        # Row 6
        CalculatorButton(self.window, "7", 7, 0, command=lambda: self.append_number("7"))
        CalculatorButton(self.window, "8", 7, 1, command=lambda: self.append_number("8"))
        CalculatorButton(self.window, "9", 7, 2, command=lambda: self.append_number("9"))
        CalculatorButton(self.window, "×", 7, 3, bg=BTN_COLOR_OP, command=lambda: self.append_operator("×"))

        # Row 7
        CalculatorButton(self.window, "4", 8, 0, command=lambda: self.append_number("4"))
        CalculatorButton(self.window, "5", 8, 1, command=lambda: self.append_number("5"))
        CalculatorButton(self.window, "6", 8, 2, command=lambda: self.append_number("6"))
        CalculatorButton(self.window, "-", 8, 3, bg=BTN_COLOR_OP, command=lambda: self.append_operator("-"))

        # Row 8
        CalculatorButton(self.window, "1", 9, 0, command=lambda: self.append_number("1"))
        CalculatorButton(self.window, "2", 9, 1, command=lambda: self.append_number("2"))
        CalculatorButton(self.window, "3", 9, 2, command=lambda: self.append_number("3"))
        CalculatorButton(self.window, "+", 9, 3, bg=BTN_COLOR_OP, command=lambda: self.append_operator("+"))

        # Row 9
        CalculatorButton(self.window, "0", 10, 0, command=lambda: self.append_number("0"))
        CalculatorButton(self.window, ".", 10, 1, command=lambda: self.append_number("."))
        CalculatorButton(self.window, "=", 10, 2, 2, width=14, bg=BTN_COLOR_EQ, command=self.calculate)

        # Row 10
        CalculatorButton(self.window, "Graph", 11, 0, 4, width=32, bg="#8e44ad", command=self.graph_equation)

        self.window.mainloop()

    def append_number(self, num):
        self.expression += str(num)
        self.input_text.set(self.expression)

    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in '+-×÷^':
            self.expression += operator
            self.input_text.set(self.expression)

    def append_function(self, func):
        if func == "sqrt":
            self.expression += "sqrt("
        elif func == '!':
            self.expression += "!"
        else:
            self.expression += ( func + "(" )
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set(self.expression)

    def delete(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def calculate(self):

        try:
            result = functions.evaluate_expression(self.expression)
            self.expression = str(result)
            self.input_text.set(self.expression)
        except Exception:
            self.expression = ""
            self.input_text.set("Error")

    def get_equation(self):
        equation = self.input_text.get()
        return equation

    def graph_equation(self):
        equation = self.get_equation()
        if equation:
            plot_equation(equation)
