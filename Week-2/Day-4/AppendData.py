import os

filename = input("Enter file name to append data: ")
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, filename)
with open(file_path, "a") as file:
    data = input("Enter text to append: ")
    file.write("\n" + data)
print("\nData appended successfully.")
with open(file_path, "r") as file:
    content = file.read()
    print("\nFull File Content (Old + New Data):")
    print(content)

