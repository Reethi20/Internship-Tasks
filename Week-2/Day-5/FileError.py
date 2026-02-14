import os
filename = input("Enter the file name to open: ")
try:
    folder_path = os.path.dirname(__file__)
    full_path = os.path.join(folder_path, filename)
    with open(full_path, "r") as file:
        content = file.read()
        print("File Content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist in this folder.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("Unexpected error:", e)

