# https://codeforces.com/problemset/problem/1971/A

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    print(f"{min(x, y)} {max(x, y)}")
