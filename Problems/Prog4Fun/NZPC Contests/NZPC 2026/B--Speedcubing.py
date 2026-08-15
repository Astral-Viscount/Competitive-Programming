# link

n = int(input())

c = list(map(int, input().split()))
m = list(map(int, input().split()))

best = 0

cur = 0
for i in range(n):
    if c[i] < m[i]:
        cur += 1
    else:
        cur = 0
    
    if cur > best:
        best = cur
        
print(best)
