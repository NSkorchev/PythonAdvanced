rows, cols = [int(el) for el in input().split(", ")]

matrix = []
max_sum = float('-inf')
submatrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        element_bellow = matrix[row_index + 1][col_index]
        next_element = matrix[row_index][col_index + 1]
        diagonal = matrix[row_index + 1][col_index + 1]
        sum_elements = current_element + next_element + diagonal + element_bellow

        if max_sum < sum_elements:
            max_sum = sum_elements
            submatrix = [[current_element, next_element], [element_bellow, diagonal]]

print(*submatrix[0])
print(*submatrix[1])
print(max_sum)