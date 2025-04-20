# https://codeforces.com/problemset/problem/617/A

distance = int(input()) 

steps = 0

for i in range(5, 0, -1):
    while distance >= i:
        distance -= i
        steps += 1

print(steps)
