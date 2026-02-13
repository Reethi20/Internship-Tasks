import os
filename = input("Enter file name to create: ")
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, filename)
with open(file_path, "w") as file:
    data = input("Enter text to write into file: ")
    file.write(data)
print("File created successfully.")

