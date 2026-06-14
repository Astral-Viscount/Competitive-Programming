#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS (AI Helped)
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(current_r, current_c):
            if not grid:
                return 0
            
            if (min(current_r, current_c) < 0 or current_r == rows or current_c == cols or (current_r, current_c) in visit or grid[current_r][current_c] == "0"):
                return 0

            visit.add((current_r, current_c))

            dfs(current_r + 1, current_c)
            dfs(current_r - 1, current_c)
            dfs(current_r, current_c + 1)
            dfs(current_r, current_c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)

        return islands
# @lc code=end

