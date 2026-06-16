# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965&page=5

c, r = map(int, input().split())

graph = [["." for i in range(c)] for _ in range(r)]

while True:
    stuff = input().split()

    if stuff[0] == "#":
        break

    symbol = stuff.pop(0)
    stuff = list(map(int, stuff))

    k = 0
    coords = []
    while k < len(stuff) - 1:
        x = stuff[k]
        y = stuff[k + 1]

        if x == 0 and y == 0:
            break
            
        coords.append((x - 1, y - 1))

        k += 2

    for nx, ny in coords:
        graph[ny][nx] = symbol

    
for row in range(r):
    print("".join(graph[row]))