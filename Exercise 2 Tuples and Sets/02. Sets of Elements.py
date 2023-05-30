n, m = [int(num) for num in input().split()]

set_n = {int(input()) for _ in range(n)}
set_m = {int(input()) for _ in range(m)}

set_z = set_n.intersection(set_m)

print(*set_z, sep='\n')

# print(set_n & set_m)
# print(set_n | set_m)
# print(set_n - set_m)
# print(set_n ^ set_m)


