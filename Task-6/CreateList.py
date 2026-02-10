n = int(input("Enter number of elements in the list: "))
lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)
print("List:", lst)
