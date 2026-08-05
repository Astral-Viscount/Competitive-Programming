#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)
        rows, cols = n, n
        
        visit = set()
        queue = deque()
        if grid[0][0] != 1 and grid[n-1][n-1] != 1:
            visit.add((0, 0))
            queue.append((0, 0))
            
            length = 1

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    if r == rows - 1 and c == cols - 1:
                        return length
                    
                    pathways = ((1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (0, -1), (-1, 0), (-1, -1))

                    for dr, dc in pathways:
                        nr, nc = dr + r, dc + c

                        if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == 1:
                            continue

                        queue.append((nr, nc))
                        visit.add((nr, nc))

                length += 1

        return -1
# @lc code=end

