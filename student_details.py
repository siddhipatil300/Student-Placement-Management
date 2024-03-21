import tkinter as tk
from tkinter import ttk
from data import DatabaseManager

class StudentDetailsWindow(tk.Toplevel):
    def __init__(self, student_id, master=None):
        super().__init__(master)
        self.title("Student Details")
        self.geometry("1200x400")  # Set a fixed window size
        self.student_id = student_id
        self.create_widgets()

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
        record = db_manager.fetch_student_by_id(self.student_id)

        if record:
            self.tree.insert("", "end", values=record)

        self.tree.pack(expand=True, fill="both")

        # Add exit button with light red background color
        exit_button = tk.Button(self, text="Exit", command=self.destroy, bg='#FF9999')
        exit_button.pack(side="bottom", padx=10, pady=10)
