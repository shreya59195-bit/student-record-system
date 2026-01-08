import csv
import os

FILE_NAME = "records.csv"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Amount"])

def add_record():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, name, amount])

    print("Record added successfully!\n")

def show_records():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)   # skip header
        print("\nID | Name | Amount")
        print("-"*25)
        for row in reader:
            print(" | ".join(row))
    print()

def delete_record():
    delete_id = input("Enter ID to delete: ")

    rows = []
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row[0] != delete_id:
                writer.writerow(row)

    print("Record deleted (if existed).\n")

def edit_record():
    edit_id = input("Enter ID to edit: ")

    rows = []
    with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

    for row in rows:
        if row[0] == edit_id:
            print("Current Name:", row[1])
            print("Current Amount:", row[2])
            row[1] = input("Enter new Name: ")
            row[2] = input("Enter new Amount: ")

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Record updated (if ID found).\n")

while True:
    print("------ MENU ------")
    print("1. Add Record")
    print("2. Show Records")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        show_records()
    elif choice == "3":
        edit_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")
