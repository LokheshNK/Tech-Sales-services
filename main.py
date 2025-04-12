import tkinter as tk
from tkinter import ttk, messagebox
from functions import TECH_SALES

# Main function to run the program
if __name__ == "__main__":
    root = tk.Tk()
    login = TECH_SALES.LoginWindow(root)
    root.mainloop()
