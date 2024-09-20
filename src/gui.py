import tkinter as tk
from tkinter import messagebox
from src.user_management import UserManagementSystem

class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management System")
        self.system = UserManagementSystem()
        self.current_user = None

        # Afficher l'interface de connexion au démarrage
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()

        self.username_label = tk.Label(self.root, text="Username")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.system.authenticate_user(username, password)
        if user is not None:
            self.current_user = user
            if self.current_user['is_admin']:
                self.show_admin_panel()
            else:
                messagebox.showinfo("Success", "Login successful! You are a regular user.")
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_admin_panel(self):
        self.clear_screen()

        self.welcome_label = tk.Label(self.root, text=f"Welcome, {self.current_user['username']} (Admin)")
        self.welcome_label.grid(row=0, column=0, columnspan=2)

        # Créer un utilisateur
        self.username_label = tk.Label(self.root, text="Username")
        self.username_label.grid(row=1, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.root, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.grid(row=3, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=3, column=1)

        self.create_button = tk.Button(self.root, text="Create User", command=self.create_user)
        self.create_button.grid(row=4, column=0, columnspan=2)

        self.list_button = tk.Button(self.root, text="List Users", command=self.list_users)
        self.list_button.grid(row=5, column=0, columnspan=2)

        # Modifier un utilisateur
        self.modify_username_label = tk.Label(self.root, text="User to Modify/Delete")
        self.modify_username_label.grid(row=6, column=0)
        self.modify_username_entry = tk.Entry(self.root)
        self.modify_username_entry.grid(row=6, column=1)

        self.new_email_label = tk.Label(self.root, text="New Email")
        self.new_email_label.grid(row=7, column=0)
        self.new_email_entry = tk.Entry(self.root)
        self.new_email_entry.grid(row=7, column=1)

        self.new_password_label = tk.Label(self.root, text="New Password")
        self.new_password_label.grid(row=8, column=0)
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.grid(row=8, column=1)

        self.modify_button = tk.Button(self.root, text="Modify User", command=self.modify_user)
        self.modify_button.grid(row=9, column=0, columnspan=2)

        self.delete_button = tk.Button(self.root, text="Delete User", command=self.delete_user)
        self.delete_button.grid(row=10, column=0, columnspan=2)

    def reset_fields(self):
        """Réinitialiser tous les champs d'entrée."""
        self.username_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.modify_username_entry.delete(0, tk.END)
        self.new_email_entry.delete(0, tk.END)
        self.new_password_entry.delete(0, tk.END)

    def create_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if username and email and password:
            self.system.create_user(username, email, password, is_admin=False)
            messagebox.showinfo("Success", "User created successfully!")
            self.reset_fields()  # Réinitialiser les champs après la création
        else:
            messagebox.showwarning("Input Error", "All fields must be filled")

    def list_users(self):
        users = self.system.list_users()
        user_list = "\n".join([f"{user['username']} - {user['email']} - Admin: {user['is_admin']}" for _, user in users.iterrows()])
        messagebox.showinfo("User List", user_list)

    def modify_user(self):
        username = self.modify_username_entry.get()
        new_email = self.new_email_entry.get()
        new_password = self.new_password_entry.get()

        if username and (new_email or new_password):
            self.system.update_user(username, new_email=new_email, new_password=new_password)
            messagebox.showinfo("Success", "User information updated successfully!")
            self.reset_fields()  # Réinitialiser les champs après modification
        else:
            messagebox.showwarning("Input Error", "You must provide a username and at least one new value")

    def delete_user(self):
        username = self.modify_username_entry.get()

        if username:
            self.system.delete_user(username)
            messagebox.showinfo("Success", "User deleted successfully!")
            self.reset_fields()  # Réinitialiser les champs après suppression
        else:
            messagebox.showwarning("Input Error", "You must provide a username to delete")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
