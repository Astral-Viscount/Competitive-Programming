# https://codeforces.com/problemset/problem/977/A

n, k = map(int, input().split())

for _ in range(k):
    num = list(str(int(n)))
    if num[-1] == '0':
        n /= 10
    else:
        n -= 1

print(int(n))
