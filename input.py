from tkinter import *


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


root.mainloop()