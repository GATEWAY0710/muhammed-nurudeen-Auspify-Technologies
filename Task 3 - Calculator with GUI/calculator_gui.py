import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("340x500")
        self.root.minsize(340, 500)
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Expression and result display
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Display frame
        display_frame = tk.Frame(root, bg="#1e1e1e")
        display_frame.pack(fill="x", padx=16, pady=(20, 12))
        
        # Result display
        display_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=("Segoe UI", 38),
            bg="#1e1e1e",
            fg="#ffffff",
            anchor="e",
            justify="right"
        )
        display_label.pack(fill="x", ipady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(root, bg="#1e1e1e")
        buttons_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        
        # Configure grid weights for even button sizing
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        
        # Button layout
        buttons = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', None]
        ]
        
        # Create buttons
        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                if btn_text is None:
                    continue
                if btn_text == '0':
                    self.create_button(buttons_frame, btn_text, r, c, colspan=1)
                else:
                    self.create_button(buttons_frame, btn_text, r, c, colspan=1)
    
    def create_button(self, frame, text, row, col, colspan=1):
        """Create calculator button."""
        # Button colors
        if text in ['C', '±', '%']:
            bg_color = "#9f9f9f"
            fg_color = "#000000"
            active_bg = "#bfbfbf"
        elif text in ['/', '*', '-', '+', '=']:
            bg_color = "#ff9f0a"
            fg_color = "#ffffff"
            active_bg = "#ffb143"
        else:
            bg_color = "#2d2d2d"
            fg_color = "#ffffff"
            active_bg = "#3d3d3d"
        
        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 20),
            bg=bg_color,
            fg=fg_color,
            activebackground=active_bg,
            activeforeground=fg_color,
            borderwidth=0,
            relief="flat",
            cursor="hand2",
            command=lambda t=text: self.button_click(t)
        )
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
    
    def button_click(self, char):
        """Handle button clicks."""
        if char == 'C':
            self.expression = ""
            self.result_var.set("0")
            return
        
        if char == '=':
            try:
                if self.expression:
                    expression_to_eval = self.expression
                    result = eval(expression_to_eval)
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)
                    self.result_var.set(str(result))
                    self.expression = str(result)
                return
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.result_var.set("0")
                return
            except Exception:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
                self.result_var.set("0")
                return
        
        if char == '±':
            try:
                if self.expression and self.expression != "0":
                    if self.expression and self.expression[0] == '-':
                        self.expression = self.expression[1:]
                    else:
                        self.expression = '-' + self.expression
                    self.result_var.set(self.expression)
            except Exception:
                pass
            return
        
        if char == '%':
            try:
                if self.expression:
                    result = float(self.expression) / 100
                    if result.is_integer():
                        result = int(result)
                    self.result_var.set(str(result))
                    self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid input")
            return
        
        # For digits and operators
        if self.expression == "0" and char in '0123456789':
            self.expression = char
        else:
            self.expression += char
        
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
