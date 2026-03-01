print("Basic Arithmetic Operations")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add=num1 + num2
sub=num1 - num2
multi=num1 * num2
print("Results")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", multi)
if num2 != 0:
    divi = num1 / num2
    print("Division:", divi)
else:
    print("Cannot divide by zero")


