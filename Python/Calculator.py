import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Refined Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#000000")  # Set background color to black

        self.current_number = ''
        self.previous_number = ''
        self.operation = None
        self.should_reset_display = False

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use the clam theme for a modern look

        # Configure styles
        self.style.configure('TButton', font=("Arial", 16), background="#000000", foreground="#FFFFFF", borderwidth=0)
        self.style.configure('Operation.TButton', foreground="#00FFFF", background="#000000")
        self.style.configure('Equals.TButton', foreground="#00FFFF", background="#000000")  # Style for "=" similar to other operators

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = ttk.Label(self.root, text="0", anchor='e', font=("Arial", 40), background="#000000", foreground="#FFFFFF")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

        # Buttons
        buttons = [
            ('C', 1, 0, "Operation.TButton"), ('%', 1, 1, "Operation.TButton"), ('⌫', 1, 2, "Operation.TButton"), ('÷', 1, 3, "Operation.TButton"),
            ('7', 2, 0, "TButton"), ('8', 2, 1, "TButton"), ('9', 2, 2, "TButton"), ('×', 2, 3, "Operation.TButton"),
            ('4', 3, 0, "TButton"), ('5', 3, 1, "TButton"), ('6', 3, 2, "TButton"), ('-', 3, 3, "Operation.TButton"),
            ('1', 4, 0, "TButton"), ('2', 4, 1, "TButton"), ('3', 4, 2, "TButton"), ('+', 4, 3, "Operation.TButton"),
            ('00', 5, 0, "TButton"), ('0', 5, 1, "TButton"), ('.', 5, 2, "TButton"), ('=', 5, 3, "Operation.TButton")
        ]

        for (text, row, col, style) in buttons:
            self.create_button(text, row, col, style)

    def create_button(self, text, row, col, style):
        button = ttk.Button(self.root, text=text, style=style, command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")  # Reduced padding
        self.root.grid_columnconfigure(col, weight=1)
        self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, char):
        if char.isdigit() or char == '.':
            self.append_number(char)
        elif char in '+-×÷':
            self.set_operation(char)
        elif char == 'C':
            self.clear_display()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.calculate()
        elif char == '%':
            self.calculate_percentage()

    def append_number(self, number):
        if self.should_reset_display:
            self.current_number = ''
            self.should_reset_display = False

        if '.' in self.current_number and number == '.':
            return

        self.current_number += number
        self.update_display()

    def update_display(self):
        display_text = self.previous_number + (self.operation if self.operation else '') + self.current_number
        self.display.config(text=display_text)

    def clear_display(self):
        self.current_number = ''
        self.previous_number = ''
        self.operation = None
        self.update_display()

    def backspace(self):
        self.current_number = self.current_number[:-1]
        self.update_display()

    def calculate_percentage(self):
        if self.current_number:
            self.current_number = str(float(self.current_number) / 100)
            self.update_display()

    def set_operation(self, op):
        if self.current_number == '' and self.previous_number == '':
            return
        if self.previous_number != '':
            self.calculate()
        self.operation = op
        self.previous_number = self.current_number or self.previous_number
        self.current_number = ''
        self.update_display()

    def calculate(self):
        if self.operation is None or self.previous_number == '':
            return

        try:
            prev = float(self.previous_number)
            current = float(self.current_number)

            if self.operation == '+':
                result = prev + current
            elif self.operation == '-':
                result = prev - current
            elif self.operation == '×':
                result = prev * current
            elif self.operation == '÷':
                result = prev / current
            else:
                return

            self.current_number = str(result)
            self.operation = None
            self.previous_number = ''
            self.should_reset_display = True
            self.update_display()
        except ValueError:
            self.clear_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
