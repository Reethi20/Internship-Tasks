numbers = [10, 20, 30, 40, 50]
try:
    position = int(input("Enter index position (0-4): "))
    print("Selected number:", numbers[position])
except ValueError:
    print("Please enter a valid integer index.")
except IndexError:
    print("Index out of range. Choose between 0 and 4.")
