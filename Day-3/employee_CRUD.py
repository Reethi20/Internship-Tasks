import sqlite3
import os

database_name = "company1.db"

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

conn.commit()

def insert_employee():
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    cursor.execute(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )
    conn.commit()
    print("Employee added.\n")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    for row in records:
        print(row)
    print()

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    salary = float(input("Enter new salary: "))
    cursor.execute(
        "UPDATE employees SET salary = ? WHERE emp_id = ?",
        (salary, emp_id)
    )
    conn.commit()
    print("Employee updated.\n")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        (emp_id,)
    )
    conn.commit()
    print("Employee deleted.\n")

while True:
    print("1. Insert")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        insert_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")

conn.close()
print("Connection closed.")