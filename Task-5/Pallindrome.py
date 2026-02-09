s = input("Enter a string: ")
start = 0
end = len(s) - 1
flag = True

while start < end:
    if s[start] != s[end]:
        flag = False
        break
    start = start + 1
    end = end - 1

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")
