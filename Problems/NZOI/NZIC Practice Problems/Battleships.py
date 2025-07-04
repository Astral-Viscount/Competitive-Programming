# https://train.nzoi.org.nz/problems/779

values = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6
}

grid = []

for i in range(10):
    arr = list(input().replace(" ", ""))
    grid.append(arr)

x, y = map(int, input().split())

while x != -1 and y != -1:
    target = grid[y][x]

    if target != "#" and values[target] == 1:
        print(f"Sunk {target}")
        del values[target]
        grid[y][x] = "#"


    elif target in values:
        print(f"Hit {target}")
        values[target] -= 1
        grid[y][x] = "#"
    
    else:
        print("Miss")

    x, y = map(int, input().split())
