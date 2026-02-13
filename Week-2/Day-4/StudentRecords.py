filename = input("Enter file name: ")
with open(filename, "a") as f:
    n = int(input("How many records? "))
    for i in range(n):
        name = input("Name: ")
        grade = input("Grade: ")
        f.write(name + "," + grade + "\n")
print("\nAll Student Records:")
with open(filename, "r") as f:
    print(f.read())
