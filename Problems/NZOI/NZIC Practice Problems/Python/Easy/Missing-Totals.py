# https://train.nzoi.org.nz/problems/631

amount = int(input())

total = 0

for i in range(amount):
    price, discount = map(int,input().split())
    if price > discount:
        total += price - discount

print(total)
