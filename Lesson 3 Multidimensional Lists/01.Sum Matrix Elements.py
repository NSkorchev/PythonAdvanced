rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

sum_nums = 0

for row_index in range(rows):
    for col_index in range(cols):
        a = 5
        sum_nums += matrix[row_index][col_index]
#matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

print(sum_nums)
print(matrix)
