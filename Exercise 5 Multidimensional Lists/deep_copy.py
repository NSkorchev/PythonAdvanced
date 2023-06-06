matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

new_matrix = matrix.copy()

new_matrix[0].append(5)

print(*matrix, sep="\n")
print()
print(*new_matrix, sep="\n")
