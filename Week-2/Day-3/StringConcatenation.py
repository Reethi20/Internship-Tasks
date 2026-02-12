"""
String Concatenation and Formatting Operations
"""

# String concatenation
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Using + operator
result = str1 + " " + str2
print("Concatenation using +:", result)

# Using join()
words = [str1, str2]
result = " ".join(words)
print("Concatenation using join():", result)

# String formatting - % operator
name = input("Enter your name: ")
age = input("Enter your age: ")
formatted = "My name is %s and I am %s years old" % (name, age)
print("Using % formatting:", formatted)

# String formatting - .format()
formatted = "My name is {} and I am {} years old".format(name, age)
print("Using .format():", formatted)

# String formatting - f-strings
formatted = f"My name is {name} and I am {age} years old"
print("Using f-strings:", formatted)
