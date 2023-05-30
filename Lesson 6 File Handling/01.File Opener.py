import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "text.txt")

try:
    file = open(file_path, "r+")
    with open(file_path, "r+") as file:
        file.writelines(["a\n", "b\n"])
    print(file.read(2))
    print("File found")
except FileNotFoundError:
    print("File not found")
# if os.path.isfile(file_path):
#     print("File found")
# else:
#     print("File not found")
#