import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack()
        
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()
        
        self.label_length = tk.Label(root, text="Password Length:")
        self.label_length.pack()
        
        self.entry_length = tk.Entry(root)
        self.entry_length.pack()
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        
        self.password_label = tk.Label(root, text="")
        self.password_label.pack()
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_fields)
        self.reset_button.pack()
        
        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password)
        self.accept_button.pack()

    def generate_password(self):
        password_length = int(self.entry_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_label.config(text=f"Generated Password: {password}")

    def reset_fields(self):
        self.entry_username.delete(0, tk.END)
        self.entry_length.delete(0, tk.END)
        self.password_label.config(text="")

    def accept_password(self):
        username = self.entry_username.get()
        password = self.password_label.cget("text").split(":")[1].strip()
        print(f"Username: {username}\nPassword: {password}")
        self.root.destroy()
if __name__ == "_main_":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
