#https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

cond = True
count = 0

for i in range(1, n + 1, 2):
    count += 1
    if count == k:
        cond = False
        print(i)
        break

if cond:
    for i in range(2, n + 1, 2):
        count += 1
        if count == k:
            print(i)
            break

