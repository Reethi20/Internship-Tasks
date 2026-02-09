# n = int(input("Enter array size: "))
# even = 0
# odd = 0
# i = 0
# while i < n:
#     x = int(input("Enter element: "))
#     if x % 2 == 0:
#         odd = odd + 1
#     else:
#         even = even + 1
#     i = i + 1
# print(even)
# print(odd)
n = int(input("Enter array size: "))
even = 0
odd = 0
i = 0
while i < n:
    x = int(input("Enter element: "))
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i + 1
print("Even",even)
print("Odd",odd)
