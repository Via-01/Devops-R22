import tkinter as tk
from tkinter import messagebox

class MyForm:
    def __init__(self, master):
        self.master = master
        master.title("My Form")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master, width=20)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(master, width=20)
        self.email_entry.grid(row=1, column=1)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=2, column=0)
        self.password_entry = tk.Entry(master, width=20, show="*")
        self.password_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, column=1)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        print("Form submitted successfully!")
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        messagebox.showinfo("Success", "Form submitted successfully!")

root = tk.Tk()
my_form = MyForm(root)
root.mainloop()