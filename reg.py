import tkinter as tk
from tkinter import messagebox

class MyForm:
    def __init__(self, master):
        self.master = master
        master.title("My Form")

        self.fields = [
            {"label": "Name:", "show": ""},
            {"label": "Email:", "show": ""},
            {"label": "Password:", "show": "*"}
        ]

        self.entries = {}

        for i, field in enumerate(self.fields):
            label = tk.Label(master, text=field["label"])
            label.grid(row=i, column=0)
            entry = tk.Entry(master, width=20, show=field["show"])
            entry.grid(row=i, column=1)
            self.entries[field["label"]] = entry

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=len(self.fields), column=1)

    def submit_form(self):
        data = {label: entry.get() for label, entry in self.entries.items()}
        print("Form submitted successfully!")
        print("Name :",data["Name:"])
        print("Email :",data["Email:"])
        print("Password :",data["Password:"])
        messagebox.showinfo("Success", "Form submitted successfully!")

root = tk.Tk()
my_form = MyForm(root)
root.mainloop()
