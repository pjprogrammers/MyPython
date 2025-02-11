import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("320x500")
        self.root.resizable(False, False)

        self.current_number = ''
        self.previous_number = ''
        self.operation = None
        self.should_reset_display = False

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Label(self.root, text="0", anchor='e', font=("Arial", 24), bg="#f0f0f0", fg="#000", height=2)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for button in buttons:
            if len(button) == 4:
                text, row, col, colspan = button
                self.create_button(text, row, col, colspan)
            else:
                text, row, col = button
                self.create_button(text, row, col, 1)

    def create_button(self, text, row, col, colspan):
        button = tk.Button(self.root, text=text, font=("Arial", 18), bg="#fff", fg="#000", bd=0, command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10, sticky="nsew")
        self.root.grid_columnconfigure(col, weight=1)
        self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, char):
        if char.isdigit() or char == '.':
            self.append_number(char)
        elif char in '+-*/':
            self.set_operation(char)
        elif char == 'C':
            self.clear_display()
        elif char == '=':
            self.calculate()

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
            elif self.operation == '*':
                result = prev * current
            elif self.operation == '/':
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
