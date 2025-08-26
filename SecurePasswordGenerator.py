"""
Python script to generate secure passwords.
The gui enables tweaking the desired password parameters

"""

import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    characters = ''
    if use_lower: characters += string.ascii_lowercase
    if use_upper: characters += string.ascii_uppercase
    if use_digits: characters += string.digits
    if use_symbols: characters += string.punctuation

    if not characters:
        result_label.config(text="Please select at least one character type!")
        copy_button.pack_forget()
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")
    copy_button.pack(pady=5)

def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated Password: ", "")
    if password and "Please select" not in password:
        pyperclip.copy(password)

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x400")

# Length spinbox with label to show value
tk.Label(root, text="Password Length:").pack(pady=5)
length_var = tk.IntVar(value=12)
length_spinbox = tk.Spinbox(root, from_=8, to=25, textvariable=length_var, width=5)
length_spinbox.pack(pady=5)
length_label = tk.Label(root, text=f"Password Length: {length_var.get()}")
length_label.pack(pady=5)

# Update label when spinbox value changes
def update_label(*args):
    length_label.config(text=f"Password Length: {length_var.get()}")
length_var.trace('w', update_label)

# Checkboxes for character types
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Lowercase (abc)", variable=lower_var).pack(pady=2)
tk.Checkbutton(root, text="Uppercase (ABC)", variable=upper_var).pack(pady=2)
tk.Checkbutton(root, text="Numbers (123)", variable=digit_var).pack(pady=2)
tk.Checkbutton(root, text="Symbols (!#$)", variable=symbol_var).pack(pady=2)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Generated Password: ")
result_label.pack(pady=20)

# Copy button (initially hidden)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack_forget()

# Start the application
root.mainloop()