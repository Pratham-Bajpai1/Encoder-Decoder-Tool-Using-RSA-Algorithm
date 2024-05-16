import tkinter as tk
from tkinter import messagebox
from rsabackend import generate_keys, encrypt, decrypt

class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption/Decryption")
        self.root.geometry("800x600")
        self.root.config(bg="#1e1e1e")

        self.create_widgets()

        # Connect to RSA backend
        self.public_key, self.private_key = generate_keys()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="RSA Encryption/Decryption", font=("Helvetica", 24, 'bold'), bg="#1e1e1e", fg="#ffffff")
        self.title_label.pack(pady=20)

        self.message_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.message_frame.pack(pady=10)

        self.message_label = tk.Label(self.message_frame, text="Enter Message:", font=("Helvetica", 14), bg="#1e1e1e", fg="#ffffff")
        self.message_label.grid(row=0, column=0, padx=5, pady=5)
        self.message_entry = tk.Entry(self.message_frame, font=("Helvetica", 14), width=40, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff")
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        self.encrypt_button = tk.Button(self.root, text="Encrypt", font=("Helvetica", 14), command=self.encrypt_message, bg="#4caf50", fg="#ffffff", activebackground="#388e3c")
        self.encrypt_button.pack(pady=10)

        self.encrypted_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#1e1e1e", fg="#ffffff", wraplength=500)
        self.encrypted_label.pack(pady=10)

        self.copy_button = tk.Button(self.root, text="Copy Encrypted Message", font=("Helvetica", 12), command=self.copy_to_clipboard, bg="#2196f3", fg="#ffffff", activebackground="#1976d2")
        self.copy_button.pack(pady=5)
        self.copy_button.config(state=tk.DISABLED)

        self.cipher_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.cipher_frame.pack(pady=10)

        self.cipher_label = tk.Label(self.cipher_frame, text="Enter Cipher (as list):", font=("Helvetica", 14), bg="#1e1e1e", fg="#ffffff")
        self.cipher_label.grid(row=0, column=0, padx=5, pady=5)
        self.cipher_entry = tk.Entry(self.cipher_frame, font=("Helvetica", 14), width=40, bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff")
        self.cipher_entry.grid(row=0, column=1, padx=5, pady=5)

        self.decrypt_button = tk.Button(self.root, text="Decrypt", font=("Helvetica", 14), command=self.decrypt_message, bg="#f44336", fg="#ffffff", activebackground="#d32f2f")
        self.decrypt_button.pack(pady=10)

        self.decrypted_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#1e1e1e", fg="#ffffff", wraplength=500)
        self.decrypted_label.pack(pady=10)

        self.footer_label = tk.Label(self.root, text="© Made by Pratham Bajpai", font=("Helvetica", 20), bg="#1e1e1e", fg="#ffffff")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def encrypt_message(self):
        message = self.message_entry.get()
        if message:
            encrypted = encrypt(message, self.public_key)
            self.encrypted_label.config(text=f"Encrypted message: {encrypted}")
            self.encrypted_message = encrypted
            self.copy_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Please enter a message to encrypt.")

    def decrypt_message(self):
        cipher = self.cipher_entry.get()
        if cipher:
            try:
                cipher_list = eval(cipher)
                decrypted = decrypt(cipher_list, self.private_key)
                self.decrypted_label.config(text=f"Decrypted message: {decrypted}")
            except:
                messagebox.showerror("Error", "Invalid cipher format. Please enter a valid list.")
        else:
            messagebox.showerror("Error", "Please enter a cipher to decrypt.")

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(str(self.encrypted_message))
        messagebox.showinfo("Copied", "Encrypted message copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAApp(root)
    root.mainloop()
