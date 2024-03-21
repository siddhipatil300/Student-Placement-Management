# import tkinter as tk
# from tkinter import messagebox
# from insert_student_data import InsertStudentDataWindow
# from view_students_placed import StudentsPlacedWindow
# from statistics import plot_statistics

# # from statistics import statistics as plot_statistics
# from grid import CompanyRecordsWindow

# def view():
#     window = StudentsPlacedWindow()

# def insert():
#     window = InsertStudentDataWindow()

# def statistics():
#     plot_statistics()

# def comp():
#     window = CompanyRecordsWindow()

# root = tk.Tk()
# root.geometry('500x300')
# root.config(bg='#f0f0f0')
# root.title("Student Placement Management System")

# # Create buttons with a specific color and font size
# view_button = tk.Button(root, text="View Student Records", command=view, width=20, bg='#4CAF50', font=('Helvetica', 14))
# view_button.pack(side="top", padx=80, pady=5, fill="x")

# insert_button = tk.Button(root, text="Insert Student Records", command=insert, width=20, bg='#2196F3', font=('Helvetica', 14))
# insert_button.pack(side="top", padx=80, pady=5, fill="x")

# # edit_button = tk.Button(root, text="Edit Student Records", command=root.destroy, width=20, bg='#3F51B5', font=('Helvetica', 14))
# # edit_button.pack(side="top", padx=80, pady=5, fill="x")

# statistics_button = tk.Button(root, text="Placement Statistics", command=statistics, width=20, bg='#009688', font=('Helvetica', 14))
# statistics_button.pack(side="top", padx=80, pady=5, fill="x")

# comp_button = tk.Button(root, text="Company Records", command=comp, width=20,bg='#00bcd4', font=('Helvetica', 14))
# comp_button.pack(side="top", padx=80, pady=5, fill="x")

# # Add exit button
# exit_button = tk.Button(root, text="Exit", command=root.destroy, bg='#FF9999', font=('Helvetica', 14))
# exit_button.pack(side="bottom", padx=80, pady=5, fill="x")

# # Start the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from insert_student_data import InsertStudentDataWindow
from view_students_placed import StudentsPlacedWindow
from statistics import plot_statistics
from grid import CompanyRecordsWindow
from student_details import StudentDetailsWindow  # Import the new window for student details

def view():
    window = StudentsPlacedWindow()

def insert():
    window = InsertStudentDataWindow()

def statistics():
    plot_statistics()

def comp():
    window = CompanyRecordsWindow()

def search_student():
    student_id = entry_search.get()
    if student_id.strip():
        student_details_window = StudentDetailsWindow(student_id)
    else:
        messagebox.showerror("Error", "Please enter a student ID.")

root = tk.Tk()
root.geometry('500x300')
root.config(bg='#f0f0f0')
root.title("Student Placement Management System")

view_button = tk.Button(root, text="View Student Records", command=view, width=20, bg='#4CAF50', font=('Helvetica', 14))
view_button.pack(side="top", padx=80, pady=5, fill="x")

insert_button = tk.Button(root, text="Insert Student Records", command=insert, width=20, bg='#2196F3', font=('Helvetica', 14))
insert_button.pack(side="top", padx=80, pady=5, fill="x")

statistics_button = tk.Button(root, text="Placement Statistics", command=statistics, width=20, bg='#009688', font=('Helvetica', 14))
statistics_button.pack(side="top", padx=80, pady=5, fill="x")

comp_button = tk.Button(root, text="Company Records", command=comp, width=20,bg='#00bcd4', font=('Helvetica', 14))
comp_button.pack(side="top", padx=80, pady=5, fill="x")

# Search Student button and entry
search_frame = tk.Frame(root)
search_frame.pack(side="top", padx=20, pady=10)

label_search = tk.Label(search_frame, text="Enter Student ID:")
label_search.pack(side="left")

entry_search = tk.Entry(search_frame)
entry_search.pack(side="left", padx=5)

search_button = tk.Button(search_frame, text="Search Student", command=search_student, bg='#00bcd4')
search_button.pack(side="left")

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg='#FF9999', font=('Helvetica', 14))
exit_button.pack(side="bottom", padx=80, pady=5, fill="x")

root.mainloop()
