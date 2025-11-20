import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica Python")
        self.root.geometry("400x600")
        self.root.configure(bg="#2c3e50")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Tela de entrada
        input_frame = self.create_display()
        input_frame.pack(side=tk.TOP)

        # Botões
        btns_frame = self.create_buttons()
        btns_frame.pack()

    def create_display(self):
        frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame.pack(side=tk.TOP)
        input_field = tk.Entry(frame, font=('arial', 24, 'bold'), textvariable=self.input_text, width=50, bg="#ecf0f1", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=15)
        return frame

    def create_buttons(self):
        frame = tk.Frame(self.root, width=400, height=450, bg="#2c3e50")
        
        # Layout dos botões
        buttons = [
            ('C', 1, 0), ('√', 1, 1), ('/', 1, 2), ('<-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('π', 5, 2), ('=', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('^', 6, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(frame, text, row, col)
        
        return frame

    def create_button(self, frame, text, row, col):
        tk.Button(frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: self.click_button(text)).grid(row=row, column=col, padx=1, pady=1)

    def click_button(self, item):
        if item == "C":
            self.expression = ""
            self.input_text.set("")
        elif item == "<-":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif item == "=":
            try:
                # Substitui simbolos visuais por operadores Python
                expr = self.expression.replace('^', '**').replace('π', 'math.pi')
                # Avalia funções trigonométricas (adiciona math.)
                expr = expr.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
                expr = expr.replace('√', 'math.sqrt')
                
                result = str(eval(expr))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Erro")
                self.expression = ""
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
    