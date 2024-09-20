from src.gui import UserManagementApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()  # Initialise la fenêtre Tkinter
    app = UserManagementApp(root)  # Crée une instance de l'application graphique
    root.mainloop()  # Démarre la boucle principale de Tkinter
