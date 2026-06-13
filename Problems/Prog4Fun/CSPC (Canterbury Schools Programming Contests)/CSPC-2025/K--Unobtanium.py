#

from collections import deque

p, x, r, c =  map(int, input().split())

grid = [[int(i) for i in input().split()] for _ in range(r)]

visit = set()
queue = deque()

queue.append((0, 0))
visit.append((0, 0))

