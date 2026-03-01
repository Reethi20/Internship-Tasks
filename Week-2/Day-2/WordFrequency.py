text = input("\nEnter a sentence: ")
words = text.split()
word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1
print("\nWord Frequency:")
print(word_count)
