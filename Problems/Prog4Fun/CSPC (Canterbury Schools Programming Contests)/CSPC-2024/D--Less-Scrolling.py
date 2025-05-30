# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=4

n, t = map(int, input().split())
days = 0

for _ in range(n):
    time_spent = sum(map(int, input().split()))
    if time_spent > t:
        days += 1

print(days)
