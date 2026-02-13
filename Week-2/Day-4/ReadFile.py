import os
filename = input("Enter file name to read: ")
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, filename)
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)
except FileNotFoundError:
    print("File does not exist in folder.")

