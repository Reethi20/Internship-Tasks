students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    age =input("Enter course: ")
    grade = input("Enter grade: ")
    students[name] = {"age": age, "grade": grade}
print("\nStudent Dictionary:")
print(students)
