s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
i = 0
while i < len(s):
    j = 0
    while j < len(vowels):
        if s[i] == vowels[j]:
            count = count + 1
        j = j + 1
    i = i + 1
print(count)
