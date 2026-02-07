print("Right triangle")
n= int(input("Enter the n(row) value: "))
for i in range(1, n+1):
    print("*" * i)
print("Inverted triangle")   
n= int(input("Enter the n(row) value: "))
for i in range(n, 0, -1):
    print("*" * i)
