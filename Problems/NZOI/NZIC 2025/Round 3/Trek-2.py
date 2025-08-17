# https://train.nzoi.org.nz/problems/1565

n = int(input())
mountains = []

for _ in range(n):
    mountains.append(int(input()))

print(max(mountains) - min(mountains))

# print(max(mountains := [int(input()) for _ in range(int(input()))]) - min(mountains))
