import tkinter as tk
from tkinter import messagebox
from insert_student_data import InsertStudentDataWindow
from view_students_placed import StudentsPlacedWindow
from statistics import statistics as plot_statistics
from grid import CompanyRecordsWindow

def view():
    window = StudentsPlacedWindow()

def insert():
    window = InsertStudentDataWindow()

def statistics():
    plot_statistics()

def comp():
    window = CompanyRecordsWindow()

root = tk.Tk()
root.geometry('500x300')
root.config(bg='#f0f0f0')
root.title("Student Placement Management System")

# Create buttons with a specific color and font size
view_button = tk.Button(root, text="View Student Records", command=view, width=20, bg='#4CAF50', font=('Helvetica', 14))
view_button.pack(side="top", padx=80, pady=5, fill="x")

insert_button = tk.Button(root, text="Insert Student Records", command=insert, width=20, bg='#2196F3', font=('Helvetica', 14))
insert_button.pack(side="top", padx=80, pady=5, fill="x")

# edit_button = tk.Button(root, text="Edit Student Records", command=root.destroy, width=20, bg='#3F51B5', font=('Helvetica', 14))
# edit_button.pack(side="top", padx=80, pady=5, fill="x")

statistics_button = tk.Button(root, text="Placement Statistics", command=statistics, width=20, bg='#009688', font=('Helvetica', 14))
statistics_button.pack(side="top", padx=80, pady=5, fill="x")

comp_button = tk.Button(root, text="Company Records", command=comp, width=20,bg='#00bcd4', font=('Helvetica', 14))
comp_button.pack(side="top", padx=80, pady=5, fill="x")

# Start the Tkinter event loop
root.mainloop()