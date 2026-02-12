# Program 2: Dictionary Operations (Add, Update, Delete, Display)
students = {}
while True:
    print("\n STUDENT DICTIONARY MENU ")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = {"grade": grade}
        print("Student added successfully!")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            students[name]["grade"] = input("Enter new grade: ")
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == 3:
        name = input("Enter student name to delete: ")
        if name in students:
            students.pop(name)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == 4:
        if students:
            print("\nStudent Details:")
            for k, v in students.items():
                print(k, "->", v)
        else:
            print("Dictionary is empty!")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
