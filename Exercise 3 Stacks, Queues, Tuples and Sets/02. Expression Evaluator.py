# from collections import deque
# from math import floor
#
# string_integers = deque(input().split())
#
# idx = 0
#
# while idx < len(string_integers):
#     element = string_integers[idx]
#
#     if element == "*":
#         for _ in range(idx - 1):
#             string_integers.appendleft(int(string_integers.popleft()) * int(string_integers.popleft()))
#     elif element == "/":
#         for _ in range(idx - 1):
#             string_integers.appendleft(int(string_integers.popleft()) / int(string_integers.popleft()))
#     elif element == "+":
#         for _ in range(idx - 1):
#             string_integers.appendleft(int(string_integers.popleft()) + int(string_integers.popleft()))
#     elif element == "-":
#         for _ in range(idx - 1):
#             string_integers.appendleft(int(string_integers.popleft()) - int(string_integers.popleft()))
#
#     if element in "*/+-":
#         del string_integers[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(string_integers[0])))

from functools import reduce
from math import floor

string_integers = input().split()

idx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, string_integers[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, string_integers[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, string_integers[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, string_integers[:i])),
}

while idx < len(string_integers):
    element = string_integers[idx]

    if element in "*/+-":
        string_integers[0] = functions[element](idx)
        [string_integers.pop(1) for i in range[idx]]
        idx = 1

    idx += 1

print(floor(int(string_integers[0])))