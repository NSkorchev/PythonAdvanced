import os

absolute_path = os.path.abspath(__file__)
file_path = os.path.join(absolute_path, "text.txt", )
print(file_path)
# file = open("text.txt", "r")
# content = file.read()
# print(content)