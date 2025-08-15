import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists.")
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location was not found.")


txt_data = "This is some text."

file_path2 = "output.txt"

with open(file_path2, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path2}' was created.")

try:
    with open(file_path2, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_path2} was not found.")