lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest = lst[0]
smallest = lst[0]
for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
