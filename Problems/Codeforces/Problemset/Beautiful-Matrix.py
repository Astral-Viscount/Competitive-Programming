# https://codeforces.com/problemset/problem/263/A

array = []
for _ in range(5):
    array.append(list(map(int, input().split()))) 

for index, arr in enumerate(array):
    if 1 in arr:
        column = index
        row = arr.index(1)

column = abs(3 - (column + 1))
row = abs(3 - (row + 1))

print(column + row)
