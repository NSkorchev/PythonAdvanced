# from collections import deque
#
# numbers = deque()
#
# for _ in range(int(input())):
#     num_data = [int(x) for x in input().split()]
#     command = num_data[0]
#
#     if command == 1:
#         numbers.append(num_data[1])
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
#
# numbers.reverse()
#
# print(*numbers, sep=", ")

from collections import deque

numbers = deque

map_functions = {
    1: lambda x: numbers.append(x[1]), # x == number_data =>[1, 97]
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    num_data = [int(x) for x in input().split()]
    map_functions[num_data[0]](num_data)

numbers.reverse()

print(*numbers, sep=", ")
