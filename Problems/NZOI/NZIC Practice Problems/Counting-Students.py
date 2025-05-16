# https://train.nzoi.org.nz/problems/35

n = int(input())

occurrences = {}

for _ in range(n):
    student = int(input())
    if student in occurrences:
        occurrences[student] += 1
    else:
        occurrences[student] = 1

duplicates = []

for student, count in occurrences.items():
    if count > 1:
        duplicates.append(student)

duplicates.sort()

for student in duplicates:
    print(student)
