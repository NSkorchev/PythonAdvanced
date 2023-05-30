import os
file_path = "Exercise 8 File Handling/files/example.txt"

with open(file_path, "w") as file:
    file.write("working with files is cool\n")

with open(file_path, "a") as file:
    file.write("just joking\n")

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "r") as file:
    print(file.readlines())

file_info = os.stat(file_path)
print(f"file size: {file_info.st_size} bytes")