rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

col_sums = []

for col_index in range(cols):
    sum_col = 0

    for rows_index in range(rows):
        sum_col += matrix[rows_index][col_index]
    col_sums.append(sum_col)

for col in col_sums:
    print(col)
