num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

primary_sum = 0
secondary = 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary += matrix[i][num - i - 1]

print(abs(primary_sum - secondary))