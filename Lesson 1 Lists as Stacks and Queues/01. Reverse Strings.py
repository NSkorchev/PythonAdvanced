text = input()
stack = list(text)

while stack:
    removed_element = stack.pop()
    print(removed_element, end='')