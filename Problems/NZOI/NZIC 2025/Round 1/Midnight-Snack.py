# https://train.nzoi.org.nz/problems/1531

n = int(input())
k = int(input())

tastiness = 0

for _ in range(n):
    t = int(input())
    if t >= k:
        tastiness += t

print(tastiness)
