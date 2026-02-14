def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Choose operation: ")
if choice == "1":
    print("Result:", add(a, b))
elif choice == "2":
    print("Result:", subtract(a, b))
elif choice == "3":
    print("Result:", multiply(a, b))
elif choice == "4":
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
