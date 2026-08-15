# https://orac2.info/problem/1463/

n = int(input())
d = list(map(int, (input().split())))

best = 0
leaders = 0

for i in d:
    if i > best:
        best = i
        leaders += 1

print(leaders)