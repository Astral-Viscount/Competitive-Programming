# https://train.nzoi.org.nz/problems/1431

n = int(input())

for _ in range(n):
    x , y = map(int, input().split())
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
        print("BLACK")
    elif (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
        print("WHITE")

