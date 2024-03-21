import tkinter as tk
from tkinter import messagebox
from data import DatabaseManager

class InsertStudentDataWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Insert Student Data")
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(1, weight=1)  # Make column resizable

        tk.Label(self, text="ID:").grid(row=0, column=0, sticky="w", padx=70, pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, sticky="ew", padx=70, pady=5)

        tk.Label(self, text="Name:").grid(row=1, column=0, sticky="w", padx=70, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, sticky="ew", padx=70, pady=5)

        tk.Label(self, text="Age:").grid(row=2, column=0, sticky="w", padx=70, pady=5)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1, sticky="ew", padx=70, pady=5)

        tk.Label(self, text="CGPI:").grid(row=3, column=0, sticky="w", padx=70, pady=5)
        self.cgpi_entry = tk.Entry(self)
        self.cgpi_entry.grid(row=3, column=1, sticky="ew", padx=70, pady=5)

        tk.Label(self, text="Skills:").grid(row=4, column=0, sticky="w", padx=70, pady=5)
        self.skills_entry = tk.Entry(self)
        self.skills_entry.grid(row=4, column=1, sticky="ew", padx=70, pady=5)

        tk.Label(self, text="Company:").grid(row=5, column=0, sticky="w", padx=70, pady=5)
        self.company_entry = tk.Entry(self)
        self.company_entry.grid(row=5, column=1, sticky="ew", padx=70, pady=5)

        insert_button = tk.Button(self, text="Insert", command=self.insert_data, bg='#009688')
        insert_button.grid(row=6, columnspan=2, sticky="ew", padx=70, pady=5)

        # Add exit button
        exit_button = tk.Button(self, text="Exit", command=self.destroy, bg='#FF9999')
        exit_button.grid(row=7, columnspan=2, sticky="ew", padx=70, pady=5)

    def insert_data(self):
        id_val = self.id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        cgpi = self.cgpi_entry.get()
        skills = self.skills_entry.get()
        company = self.company_entry.get()  # Retrieve company value

        db_manager = DatabaseManager('placed.db')
        db_manager.insert_student(id_val, name, age, cgpi, skills, company)
        messagebox.showinfo("Success", "Student data inserted successfully!")
        self.destroy()
