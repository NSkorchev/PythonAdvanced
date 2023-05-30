row = int(input())

# matrix = []
flatten = []

for _ in range(row):
    inner_list = [int(el) for el in input().split(", ")]
    flatten.extend(inner_list)

# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         flatten.append(matrix[row_index][col_index])

print(flatten)