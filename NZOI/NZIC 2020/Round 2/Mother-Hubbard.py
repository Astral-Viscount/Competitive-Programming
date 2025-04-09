# https://train.nzoi.org.nz/problems/1164

n = int(input())

childrens = 10

for i in range(n):
    child = int(input())
    childrens += child

if childrens == 10:
    print("She's got them all")
else:
    print(10 - childrens)
