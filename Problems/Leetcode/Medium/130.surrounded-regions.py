#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(current_r, current_c):
            if min(current_r, current_c) < 0 or current_r == rows or current_c == cols or board[current_r][current_c] != 'O':
                return 0
            
            board[current_r][current_c] = 'T'

            dfs(current_r + 1, current_c)
            dfs(current_r - 1, current_c)
            dfs(current_r, current_c + 1)
            dfs(current_r, current_c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows - 1] or c in [0, cols - 1]) and board[r][c] == 'O':
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        
# @lc code=end

