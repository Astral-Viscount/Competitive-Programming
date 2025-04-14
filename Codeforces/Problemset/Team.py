# https://codeforces.com/problemset/problem/231/A

n = int(input())

count = 0

for _ in range(n):
    if sum(list(map(int, input().split()))) >= 2:
        count += 1

print(count)
