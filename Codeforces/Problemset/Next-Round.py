# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

participants = 0
threshold = a[k - 1]

for i in a:
    if i >= threshold and i > 0:
        participants += 1
    else:
        break

print(participants)
