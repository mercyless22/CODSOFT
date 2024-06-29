import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(simpledialog.askstring("Input", "Enter the desired password length:"))
        if length < 1:
            raise ValueError("Length must be a positive integer")
        
        # Create a pool of characters
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # Generate password
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Display the generated password
        password_label.config(text=password)
    except ValueError as e:
        messagebox.showerror("Input error", str(e))

def copy_to_clipboard():
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copy to clipboard", "Password copied to clipboard")
    else:
        messagebox.showerror("Copy error", "No password to copy")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.minsize(400, 200)  # Set a minimum size for the window

# Create and place the button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Create and place the label to display the password
password_label = tk.Label(root, text="", font=("Helvetica", 16))
password_label.pack(pady=10)

# Create and place the button to copy the password with "Ctrl+C" text
copy_button = tk.Button(root, text="Copy Password (Ctrl+C)", command=copy_to_clipboard)
copy_button.pack(pady=20)

# Start the application
root.mainloop()
