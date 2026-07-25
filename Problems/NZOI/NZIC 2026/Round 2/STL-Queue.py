# https://train.nzoi.org.nz/problems/1719

n = int(input())

members = [input() for _ in range(n)]

for idx, member in enumerate(members):
    if member == "G":
        print(idx + 1)

for idx, member in enumerate(members):
    if member == "S":
        print(idx + 1)

for idx, member in enumerate(members):
    if member == "B":
        print(idx + 1)