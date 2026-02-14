file_path = "records.txt"  
while True:
    print("\n1.Add  2.View  3.Delete  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        with open(file_path, "a") as f:
            f.write(f"{name},{age}\n")
        print("Record added!")
    elif choice == "2":
        try:
            with open(file_path, "r") as f:
                data = f.read()
                print("\nRecords:\n", data if data else "No records found.")
        except FileNotFoundError:
            print("File not found.")
    elif choice == "3":
        name_del = input("Enter name to delete: ")
        try:
            with open(file_path, "r") as f:
                lines = f.readlines()

            with open(file_path, "w") as f:
                for line in lines:
                    if not line.startswith(name_del + ","):
                        f.write(line)

            print("Record deleted (if existed).")
        except FileNotFoundError:
            print("File not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
