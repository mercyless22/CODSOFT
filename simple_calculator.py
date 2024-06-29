import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math error", "Cannot divide by zero")
        else:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Set up the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.minsize(400, 200)  # Set a minimum size for the window

# Configure grid layout to distribute columns evenly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Create and place the input fields and labels with padding
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='ew')
entry1 = tk.Entry(root)
entry1.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky='ew')

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='ew')
entry2 = tk.Entry(root)
entry2.grid(row=1, column=2, padx=10, pady=10, columnspan=2, sticky='ew')

# Create and place the buttons for each operation with padding and symbols in a single row
tk.Button(root, text="+", command=add, width=5).grid(row=2, column=0, padx=10, pady=10, sticky='ew')
tk.Button(root, text="-", command=subtract, width=5).grid(row=2, column=1, padx=10, pady=10, sticky='ew')
tk.Button(root, text="*", command=multiply, width=5).grid(row=2, column=2, padx=10, pady=10, sticky='ew')
tk.Button(root, text="/", command=divide, width=5).grid(row=2, column=3, padx=10, pady=10, sticky='ew')

# Create and place the result label, spanning across all columns
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Start the application
root.mainloop()
