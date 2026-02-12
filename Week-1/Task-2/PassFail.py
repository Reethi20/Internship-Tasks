marks = int(input("Enter your marks (0 to 100): "))
if marks>=40 and marks<=100:
    print("Pass")
elif marks < 40:
    print("Fail")
else:
    print("Invalid marks! Please enter between 0 and 100.")

