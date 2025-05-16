# https://codeforces.com/contest/863/problem/B

n = int(input())
weights = sorted(list(map(int, input().split())))

min_diff = float('inf')

for i in range(2 * n):
    for j in range(i + 1):
        if weights[i] == weights[j]:
            min_diff = min(abs(weights[i + 1] - weights[j + 1]), min_diff)

print(min_diff)
            