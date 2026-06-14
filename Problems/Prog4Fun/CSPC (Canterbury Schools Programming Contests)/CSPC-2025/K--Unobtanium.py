# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=3&mdlscrollto=1126.4000244140625

from collections import deque

p, x, c, r =  map(int, input().split())

grid = [[int(i) for i in input().split()] for _ in range(r)]

def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    
    visit = set()
    queue = deque()

    queue.append((0, 0))
    visit.add((0, 0))

    length = 0

    while queue:
        for _ in range(len(queue)):
            curr_r, curr_c = queue.popleft()
            
            if curr_r == rows - 1 and curr_c == cols - 1:
                return length

            neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbours:
                nr, nc = curr_r + dr, curr_c + dc

                if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == 1:
                    continue
                    
                queue.append((nr, nc))
                visit.add((nr, nc))
        
        length += 1

path = bfs(grid)
cost = path * x

if cost > (p // 2):
    print("Don't take the contract!")
else:
    print(p - cost)

