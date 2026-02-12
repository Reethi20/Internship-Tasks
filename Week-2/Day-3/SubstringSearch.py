"""
Substring Search and Pattern Matching
"""

text = input("Enter a string: ")
substring = input("Enter substring to search: ")

print("\n--- Substring Search ---")
print(f"Text: '{text}'")
print(f"Substring: '{substring}'")

if substring in text:
    print(f"'{substring}' found in '{text}'")
    print(f"Position: {text.index(substring)}")
    print(f"Occurrences: {text.count(substring)}")
else:
    print(f"'{substring}' NOT found in '{text}'")

print("\n--- All Positions ---")
substring_in = input("Enter substring to find all positions: ")
count = 0
start = 0
positions = []
while True:
    pos = text.find(substring_in, start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1
    count += 1

if positions:
    print(f"Found '{substring_in}' at positions: {positions}")
else:
    print(f"'{substring_in}' not found")

print("\n--- Pattern Examples ---")
print("Contains 'a':", 'a' in text.lower())
print("Contains digit:", any(c.isdigit() for c in text))
print("Contains space:", ' ' in text)
print("Contains uppercase:", any(c.isupper() for c in text))
print("Contains lowercase:", any(c.islower() for c in text))
