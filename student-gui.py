import json
import os
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

JSON_FILE = "students.json"
CSV_FILE = "students.csv"

# ------------------ Data Handling ------------------

def load_data():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)
    # Also save to CSV 
    save_to_csv(data)  

def save_to_csv(data):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "name", "course", "marks"]
        )

        writer.writeheader()
        writer.writerows(data)


# ------------------ Student Operations ------------------

def add_student():
    id = simpledialog.askstring("id", "Enter id ")
    name = simpledialog.askstring("Name", "Enter Student Name")
    course = simpledialog.askstring("Course", "Enter Course")
    marks = simpledialog.askstring("Marks", "Enter Marks")

    if not id or not name:
        messagebox.showwarning("Error", "id & Name are required")
        return

    students = load_data()

    for s in students:
        if s["id"] == id:
            messagebox.showerror("Error", " id already exists")
            return

    students.append({
        "id": id,
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
            f"id: {s['id']} | Name: {s['name']} | Course: {s['course']} | Marks: {s['marks']}"
        )

def delete_student():
    id = simpledialog.askstring("Delete", "Enter id to delete")

    students = load_data()
    new_data = [s for s in students if s["id"] != id]

    if len(students) == len(new_data):
        messagebox.showerror("Error", "id not found")
        return

    save_data(new_data)
    messagebox.showinfo("Deleted", "Record deleted")
    show_students()

def normalize_data(data):
    fixed = []
    for s in data:
        fixed.append({
            "id": s.get("id", s.get("roll", "")),
            "name": s.get("name", ""),
            "course": s.get("course", ""),
            "marks": s.get("marks", "")
        })
    return fixed

def load_data():
    if not os.path.exists(JSON_FILE):
        return []

    with open(JSON_FILE, "r") as f:
        data = json.load(f)

    data = normalize_data(data)   # convert old → new
    save_data(data)               # rewrite clean data
    return data


# ------------------ GUI Window ------------------

window = tk.Tk()
window.title("Student Record Manager")
window.geometry("600x400")

title = tk.Label(window, text="Student Record System", font=("Arial", 18))
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
