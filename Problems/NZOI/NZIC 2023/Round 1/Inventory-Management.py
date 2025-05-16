# https://train.nzoi.org.nz/problems/1314

k, n = map(int, input().split())
d = list(map(int, input().split()))

d.sort(reverse=True)

zombies = 0

if n <= k:
    for i in range(n):
        zombies += d[i]
else:
    for j in range(k):
        zombies += d[j]

print(zombies)
