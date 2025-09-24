import tkinter as tk
from vigenere import encrypt, decrypt

def run_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    key = entry_key.get().strip()
    output.delete("1.0", tk.END)
    output.insert(tk.END, encrypt(text, key))

def run_decrypt():
    text = entry_text.get("1.0", tk.END).strip()
    key = entry_key.get().strip()
    output.delete("1.0", tk.END)
    output.insert(tk.END, decrypt(text, key))

root = tk.Tk()
root.title("Vigenere Cipher")

# Input text
tk.Label(root, text="Enter Text:").pack()
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

# Key input
tk.Label(root, text="Enter Key:").pack()
entry_key = tk.Entry(root)
entry_key.pack()

# Buttons
tk.Button(root, text="Encrypt", command=run_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=run_decrypt).pack(pady=5)

# Output box
tk.Label(root, text="Result:").pack()
output = tk.Text(root, height=5, width=40)
output.pack()

root.mainloop()
