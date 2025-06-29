n = int(input())
s = input()

smallest = min(s)
position = []

for i, j in enumerate(s):
    if j == smallest:
        position.append(i)

best = s

for k in position:
    sliced = s[k:] + s[:k]
    if sliced < best:
        best = sliced

print(best)