def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        return "Divide by Zero not Possible"
    else:
        return a / b

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))
