string = input("Enter a string: ")
string = string.lower()

reverse = ""
for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
