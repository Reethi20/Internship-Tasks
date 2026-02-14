balance = float(input("Enter initial balance: "))

while True:
    print("\n Bank System ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful!")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
