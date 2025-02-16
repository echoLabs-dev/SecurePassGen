import tkinter as tk
import string
import random
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password length must be at least 4!")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Tkinter UI
root = tk.Tk()
root.title("SecurePassGen")
root.geometry("350x250")

# Password length label and input
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_var = tk.IntVar(value=12)
tk.Entry(root, textvariable=length_var, width=5, font=("Arial", 12)).pack(pady=5)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=10)

# Password display field
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12), state="readonly").pack(pady=5)

# Copy button
tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Arial", 12)).pack(pady=10)

root.mainloop()
