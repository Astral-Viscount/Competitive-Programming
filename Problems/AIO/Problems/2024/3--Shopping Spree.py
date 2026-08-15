# https://orac2.info/problem/1465/

n , k = map(int, input().split())
c = list(map(int, input().split()))

cost = 0 

for i in range(k):
    cost += c[i]

for j in range(k, n - k, 2):
    cost += c[j + 1]

print(cost)