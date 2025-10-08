# https://train.nzoi.org.nz/problems/799

def missing_num(nums, r):
    total = 0
    for i in range(1, r + 1):
        total += i

    num = total - sum(nums)
    return num

r, c = map(int, input().split())

nums = []

grid = []

for _ in range(r):
    axis = list(input().split())

    if "x" in axis:
        axis[axis.index('x')] = '0'
    arr = [int(i) for i in axis]
    grid.append(arr)

index1 = None
index2 = None

for row, column in enumerate(grid):
    if 0 in column:
        index1 = row
        index2 = column.index(0)
        break

for i in grid:
    value = i[index2]
    if value != 0:
        nums.append(value)


num = missing_num(nums, r)

grid[index1][index2] = num

for ro in grid:
    for col in ro:
        print(col, end=" ")
    print()

""" Better Way to Output (Probably(IDK))
for ro in grid:
    ro = [str(i) for i in ro]
    print(" ".join(ro))
"""
