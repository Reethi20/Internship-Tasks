n = int(input("Enter the number of Fibonacci numbers to generate: "))
a = 0
b = 1
i = 0

while i < n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1
