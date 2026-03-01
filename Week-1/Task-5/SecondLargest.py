n = int(input("Enter the number of elements: "))
arr = []
i = 0
while i < n:
    arr.append(int(input("Enter element: ")))
    i = i + 1

largest = arr[0]
second = -999999999

i = 1
while i < n:
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]
    i = i + 1

print(second)
