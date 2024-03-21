import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class CompanyRecordsWindow:
    def __init__(self):
        self.root = ThemedTk(theme="arc")
        self.root.title("Company Records")
        self.root.geometry("900x500")  # Set a fixed window size

        self.table = ttk.Treeview(self.root, columns=("Serial No.", "Package", "Skill Set Required"))
        self.table.heading("#0", text="Serial No.")
        self.table.heading("Serial No.", text="Serial No.")
        self.table.heading("Package", text="Package")
        self.table.heading("Skill Set Required", text="Skill Set Required")
        
        data = [
            ("1", "M&Ms", "5 lakhs", "Python, SQL"),
            ("2", "JK", "4 lakhs", "Java, C++"),
            ("3", "MK", "7 lakhs", "Python, Django"),
            ("4", "XYZ Corp", "6 lakhs", "JavaScript, HTML, CSS"),
            ("5", "ABC Solutions", "8 lakhs", "Python, Flask"),
            ("6", "Tech Innovators", "10 lakhs", "Java, Spring"),
            ("7", "Tech Wizards", "9 lakhs", "C#, .NET"),
            ("8", "DataCraft", "7.5 lakhs", "R, MATLAB"),
            ("9", "CodeNinjas", "6.5 lakhs", "Ruby, Rails"),
            ("10", "WebWeavers", "8.5 lakhs", "PHP, Laravel"),
            ("11", "AI Solutions", "12 lakhs", "Machine Learning, TensorFlow"),
            ("12", "CyberSec Ltd.", "11 lakhs", "Cybersecurity, Penetration Testing"),
            ("13", "CloudWorks", "10 lakhs", "AWS, Azure"),
            ("14", "GameGenius", "8 lakhs", "Unity, Unreal Engine"),
            ("15", "MobileMasters", "9.5 lakhs", "iOS, Android")
        ]

        for item in data:
            self.table.insert("", "end", text=item[0], values=(item[1], item[2], item[3]))

        self.table.pack(fill="both", expand=True)

        # Add exit button with light red background color
        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, bg='#FF9999')
        exit_button.pack(side="bottom", padx=10, pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    window = CompanyRecordsWindow()
