# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=8

n = int(input())

students = {}

for _ in range(n):
    name, x, y, z = input().split()

    x = int(x)
    y = int(y)
    z = int(z)

    avg = (x + y + z) / 3

    students[name] = avg

max_value = max(students.values())

for key, value in students.items():
    if value == max_value:
        print(key)
