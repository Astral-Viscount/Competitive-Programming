# https://train.nzoi.org.nz/problems/1669

n = int(input())
k = int(input())

skill = [int(input()) for _ in range(n)]
skill.sort()

count = 0
curr = 0
for s in skill:
    if curr + s <= k:
        curr += s
        count += 1
    else:
        break

print(count)
