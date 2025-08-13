# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9493&cmid=3529&page=1

names = list(input().split())
n = int(input())

for _ in range(n):
    pos_a, pos_b = map(int, input().split())
    names[pos_a - 1], names[pos_b - 1] = names[pos_b - 1], names[pos_a - 1]

print(" ".join(names))