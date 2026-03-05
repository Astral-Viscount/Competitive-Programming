# https://train.nzoi.org.nz/problems/687

n = int(input())
a, b, c, d = map(int, input().split())

john = 0
mary = 0
john_counter = 0
mary_counter = 0

while john_counter < n:
    john_counter += a
    john += 1
    if john_counter < n:
        john_counter += b
        john += 1


while mary_counter < n:
    mary_counter += c
    mary += 1
    if mary_counter < n:
        mary_counter += d
        mary += 1

print(mary - john)