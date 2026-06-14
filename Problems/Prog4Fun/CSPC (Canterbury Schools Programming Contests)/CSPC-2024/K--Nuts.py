# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11310&cmid=4328&page=11

from collections import deque

x, y, g = map(int, input().split())

grid = [[int(x) for x in input().split()] for _ in range(g)]

def bfs(grid):

    if grid[0][0] == 0 or grid[y][x] == 0:
        return -1

    visit = set()
    queue = deque()

    queue.append((0, 0))
    visit.add((0, 0))

    jumps = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            if r == y and c == x:
                return jumps
            
            neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr == g or nc == g or (nr, nc) in visit or grid[nr][nc] == 0:
                    continue

                queue.append((nr, nc))
                visit.add((nr, nc))
        
        jumps += 1
        
    return -1

jump = bfs(grid)

if jump == -1:
    print("Tim is gonna get real hungry today!")
else:
    print(f"Tim needs to jump {jump} times.")