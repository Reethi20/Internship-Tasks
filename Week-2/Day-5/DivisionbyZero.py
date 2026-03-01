try:
    x = float(input("Enter numerator: "))
    y = float(input("Enter denominator: "))
    result = x / y
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
