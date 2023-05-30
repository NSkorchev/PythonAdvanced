from statistics import mean
from collections import defaultdict
n = int(input())
student_grades = defaultdict(lambda: [])

for _ in range(n):

    name, grade = tuple(input().split())
    grade = float(grade)
    # if name not in student_grades:
    #     student_grades[name] = []
    student_grades[name].append(grade)


for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    print(f'{name} -> {" ".join([str(f"{grade:.2f}") for grade in grades])} (avg: {avg:.2f})')