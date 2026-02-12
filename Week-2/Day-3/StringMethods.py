"""
String Methods and Operations
"""

text = input("Enter a string: ")

print("Original string:", text)
print("\n--- Finding ---")
print("Find 'a':", text.find('a'))
print("Find 'x':", text.find('x'))

print("\n--- Counting ---")
print("Count of 'a':", text.count('a'))

print("\n--- Replacing ---")
print("Replace 'a' with 'x':", text.replace('a', 'x'))

print("\n--- Splitting ---")
print("Split by space:", text.split(' '))

print("\n--- Joining ---")
words = ['Hello', 'World', 'Python']
print("Join words:", ' '.join(words))

print("\n--- Trimming ---")
text_with_spaces = "  Hello World  "
print("Original with spaces: '" + text_with_spaces + "'")
print("After strip():", "'" + text_with_spaces.strip() + "'")
print("After lstrip():", "'" + text_with_spaces.lstrip() + "'")
print("After rstrip():", "'" + text_with_spaces.rstrip() + "'")

print("\n--- Checking ---")
print("Starts with 'H':", text.startswith('H') if text else False)
print("Ends with 'o':", text.endswith('o') if text else False)
print("Is alpha:", text.isalpha())
print("Is digit:", text.isdigit())
print("Is alphanumeric:", text.isalnum())
