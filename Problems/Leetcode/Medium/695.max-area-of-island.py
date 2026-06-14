#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(current_r, current_c):
            
            if min(current_r, current_c) < 0 or (current_r, current_c) in visit or current_r == rows or current_c == cols or grid[current_r][current_c] == 0:
                return 0
            
            visit.add((current_r, current_c))

            return (1 + 
                    dfs(current_r + 1, current_c) +
                    dfs(current_r - 1, current_c) +
                    dfs(current_r, current_c + 1) +
                    dfs(current_r, current_c - 1)
            )
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    curr_area = dfs(r, c)
                    area = max(area, curr_area)

        return area
# @lc code=end

