numbers = tuple([float(num) for num in input().split()])
occ = {}

for num in numbers:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for num, count in occ.items():
    print(f"{num} - {count} times")