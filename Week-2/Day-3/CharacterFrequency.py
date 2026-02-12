string = input("Enter a string: ")
frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character Frequency:")
for key, value in frequency.items():
    print(key, ":", value)
