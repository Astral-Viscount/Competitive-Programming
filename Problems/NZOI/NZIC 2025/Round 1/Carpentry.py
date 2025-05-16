# https://train.nzoi.org.nz/problems/1449

n = int(input())
height = sorted(list(map(int, input().split())))

stair = 0

for i in height:
    if i >= stair + 1:
        stair += 1

print(stair)