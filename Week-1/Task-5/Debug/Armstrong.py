# n = int(input("Enter a number: "))
# temp = n
# sum = 0
# while n > 0:
#     sum = (n % 10) * 3
#     n = n // 10
# if sum == temp:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
n = int(input("Enter a number: "))
temp = n
sum = 0
while n > 0:
    d = n % 10
    sum = sum + d * d * d
    n = n // 10
if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
