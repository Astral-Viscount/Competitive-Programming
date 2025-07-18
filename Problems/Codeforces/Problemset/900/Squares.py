# https://codeforces.com/problemset/problem/1351/B

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    h1 = max(a, b)
    w1 = min(a, b)

    h2 = max(c, d)
    w2 = min(c, d)

    if h1 == h2 and (w1 + w2) == h1:
        print("Yes")
    else:
        print("No")
