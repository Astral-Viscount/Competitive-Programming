# https://train.nzoi.org.nz/problems/1538

n = int(input())
segment = sorted(list(map(int, input().split())))
cans = sorted(list(map(int, input().split())))

best = 0

for i in range(n):
    best += abs(segment[i] - cans[i])

print(best)
