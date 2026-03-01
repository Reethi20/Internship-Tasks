import os
filename = input("Enter file name: ")
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
with open(path, "a") as f:
    n = int(input("How many records? "))
    for i in range(n):
        name = input("Name: ")
        grade = input("Grade: ")
        f.write(name + "," + grade + "\n")

print("\nAll Student Records:")
with open(path, "r") as f:
    print(f.read())
