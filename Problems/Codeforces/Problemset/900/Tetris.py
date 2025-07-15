# https://codeforces.com/problemset/problem/961/A

n , m  = map(int, input().split())
blocks = list(map(int, input().split()))

columns = [0] * (n + 1)

for block in blocks:
    columns[block] += 1

appearance = float('inf')

for i in range(1, n + 1):
    appearance = min(appearance, columns[i])

print(appearance)
