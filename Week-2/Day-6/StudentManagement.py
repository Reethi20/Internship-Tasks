students = []
while True:
    print("\n Student Management System ")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")
        students.append({"name": name, "roll": roll, "marks": marks})
        print("Student added successfully!")

    elif choice == "2":
        if students:
            for s in students:
                print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
        else:
            print("No students available.")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False
        for s in students:
            if s["roll"] == roll:
                print("Student Found:", s)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to delete: ")
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
