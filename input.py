from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Student Management System")


frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

Label(frame, text="Name: ").grid(row=0, column=0, padx=2, sticky="w")
name_entry = Entry(frame).grid(row=0, column=1, pady=2, sticky="ew")

Label(frame, text="Address: ").grid(row=1, column=0, padx=2, sticky="w")
address_entry = Entry(frame).grid(row=1, column=1, pady=2, sticky="ew")

Label(frame, text="Age: ").grid(row=2, column=0, padx=2, sticky="w")
age_entry = Entry(frame).grid(row=2, column=1, pady=2, sticky="ew")

Label(frame, text="Phone Number: ").grid(row=3, column=0, padx=2, sticky="w")
phone_entry = Entry(frame).grid(row=3, column=1, pady=2, sticky="ew")


button_frame = Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

Button(button_frame, text="Create Table").grid(row=0, column=0, padx=5)
Button(button_frame, text="Add Data").grid(row=0, column=1, padx=5)
Button(button_frame, text="Update Data").grid(row=0, column=2, padx=5)
Button(button_frame, text="Delete Data").grid(row=0, column=3, padx=5)


tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)


root.mainloop()