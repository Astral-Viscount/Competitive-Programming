# https://train.nzoi.org.nz/problems/1257

n = int(input())
flowers = list(input().strip())

change = 0

for i in range(n - 1):
    if flowers[i] == flowers[i + 1]:
        change += 1

