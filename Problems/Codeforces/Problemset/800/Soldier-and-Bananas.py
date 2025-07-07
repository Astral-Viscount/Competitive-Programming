# https://codeforces.com/problemset/problem/546/A

cost, money, amount = map(int, input().split())

final_cost = 0

for i in range(1, amount + 1):
    final_cost += cost * i

if final_cost >= money:
    print(final_cost - money)
else:
    print(0)
