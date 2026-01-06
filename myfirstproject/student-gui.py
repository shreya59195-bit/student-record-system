import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    roll = simpledialog.askstring("Roll No", "Enter Roll Number")
    name = simpledialog.askstring("Name", "Enter Student Name")
    course = simpledialog.askstring("Course", "Enter Course")
    marks = simpledialog.askstring("Marks", "Enter Marks")

    if not roll or not name:
        messagebox.showwarning("Error", "Roll No & Name are required")
        return

    students = load_data()

    for s in students:
        if s["roll"] == roll:
            messagebox.showerror("Error", "Roll number already exists")
            return

    students.append({
        "roll": roll,
        "name": name,
        "course": course,
        "marks": marks
    })

    save_data(students)
    messagebox.showinfo("Success", "Student added successfully")
    show_students()

def show_students():
    students = load_data()

    listbox.delete(0, tk.END)

    if not students:
        listbox.insert(tk.END, "No records found")
        return

    for s in students:
        listbox.insert(
            tk.END,
            f"Roll: {s['roll']} | Name: {s['name']} | Course: {s['course']} | Marks: {s['marks']}"
        )

def delete_student():
    roll = simpledialog.askstring("Delete", "Enter Roll No to delete")

    students = load_data()
    new_data = [s for s in students if s["roll"] != roll]

    if len(students) == len(new_data):
        messagebox.showerror("Error", "Roll number not found")
        return

    save_data(new_data)
    messagebox.showinfo("Deleted", "Record deleted")
    show_students()


# ---------- GUI Window ----------
window = tk.Tk()
window.title("Student Record Manager")
window.geometry("600x400")

title = tk.Label(window, text="Student Record System",
                 font=("Arial", 18))
title.pack(pady=10)

listbox = tk.Listbox(window, width=80, height=12)
listbox.pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

btn_add = tk.Button(btn_frame, text="Add Student", width=15, command=add_student)
btn_add.grid(row=0, column=0, padx=5)

btn_show = tk.Button(btn_frame, text="Show Records", width=15, command=show_students)
btn_show.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(btn_frame, text="Delete Record", width=15, command=delete_student)
btn_delete.grid(row=0, column=2, padx=5)

show_students()
window.mainloop()
