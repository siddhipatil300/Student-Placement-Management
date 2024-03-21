import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data import DatabaseManager

class StudentsPlacedWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Students Placed")
        self.geometry("1200x500")  # Set a fixed window size
        self.create_widgets()

        # Bind the event handler to window resize event
        self.bind("<Configure>", self.on_window_resize)

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("ID", "Name", "Age", "CGPI", "Skills", "Company")
        self.tree.heading("#0", text="Index")
        self.tree.column("#0", minwidth=0, width=50)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("CGPI", text="CGPI")
        self.tree.heading("Skills", text="Skills")
        self.tree.heading("Company", text="Company")

        db_manager = DatabaseManager('placed.db')
        self.records = db_manager.fetch_students_placed()

        for i, record in enumerate(self.records, start=1):
            self.tree.insert("", "end", text=str(i), values=record)

        self.tree.pack(expand=True, fill="both")

        # Add Exit button
        exit_button = tk.Button(self, text="Exit", command=self.destroy, bg='#FF9999')
        exit_button.pack(side="bottom", padx=10, pady=10)

    def on_window_resize(self, event):
        # Adjust the size of the Treeview widget when the window is resized
        self.tree.pack_configure(expand=True, fill="both")
