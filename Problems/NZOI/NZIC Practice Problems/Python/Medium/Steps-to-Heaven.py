# https://train.nzoi.org.nz/problems/687

n = int(input())
a, b, c, d = map(int, input().split())

john = 0
mary = 0
john_step = 0
mary_step = 0

while john_step < n:
    john_step += a
    john += 1
    if john_step >= n:
        break
    john_step += b
    john += 1


while mary_step < n:
    mary_step += c
    mary += 1
    if mary_step >= n:
        break
    mary_step += d
    mary += 1

print(mary - john)