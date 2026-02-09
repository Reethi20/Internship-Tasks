s = input("Enter a string: ")
rev = ""
i = len(s) - 1

while i >= 0:
    rev = rev + s[i]
    i = i - 1

print(rev)
