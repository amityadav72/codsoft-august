import tkinter as tk

def on_number_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def on_operation_click(operation):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + " " + operation + " ")

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Number buttons
button_labels = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]
row_num = 1
col_num = 0
for label in button_labels:
    btn = tk.Button(root, text=label, padx=20, pady=20, font=("Arial", 20), command=lambda label=label: on_number_click(label))
    btn.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Operation buttons
operations = ['+', '-', '*', '/']
for i, operation in enumerate(operations):
    btn = tk.Button(root, text=operation, padx=20, pady=20, font=("Arial", 20), command=lambda operation=operation: on_operation_click(operation))
    btn.grid(row=i + 1, column=3)

# Equals button
btn_equals = tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 20), command=calculate)
btn_equals.grid(row=4, column=2)

# Clear button
btn_clear = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 20), command=clear)
btn_clear.grid(row=4, column=1, columnspan=1)

root.mainloop()
