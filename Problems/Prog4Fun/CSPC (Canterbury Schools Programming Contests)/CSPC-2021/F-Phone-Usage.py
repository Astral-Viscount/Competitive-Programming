# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11313&cmid=1851&page=6

n = int(input())

minutes = 0

for _ in range(n):
    x, s, e = map(int, input().split())
    minutes += e - s

print(minutes)