def find_element(matrix, element):
    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == element:
                return (row_index, col_index)


n = int(input())
matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
position = find_element(matrix, searched_symbol)

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")