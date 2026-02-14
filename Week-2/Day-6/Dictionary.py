dictionary = {}

while True:
    print("\n1.Search  2.Add  3.Delete  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        word = input("Enter word: ").lower()
        print("Meaning:", dictionary.get(word, "Word not found"))

    elif choice == "2":
        word = input("Enter new word: ").lower()
        meaning = input("Enter meaning: ")
        dictionary[word] = meaning
        print("Word added!")

    elif choice == "3":
        word = input("Enter word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word deleted!")
        else:
            print("Word not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
