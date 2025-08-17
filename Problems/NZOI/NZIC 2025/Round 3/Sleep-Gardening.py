# https://train.nzoi.org.nz/problems/1363

n, m, k = map(int, input().split())
p, h = map(int, input().split())

best = max((n - p), (p - 1))

height = max((h + best), n)

print(height)