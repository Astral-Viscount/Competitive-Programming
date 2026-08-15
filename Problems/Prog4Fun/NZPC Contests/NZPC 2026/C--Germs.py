# link

n, r = map(int, input().split())
bacterias = list(map(int, input().split()))

best = float('inf')

for i in range((n - r) + 1):
    cur = sum(bacterias[i:i+r])

    if cur < best:
        best = cur

print(best)    
