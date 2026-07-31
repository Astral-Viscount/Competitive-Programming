#
# @lc app=leetcode id=3248 lang=python3
#
# [3248] Snake in Matrix
#

# @lc code=start
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # matrix = [[(i * n) + j for j in range(n)] for i in range(n)]
        
        row, col = 0, 0

        for command in commands:
            if command == "RIGHT":
                col += 1
            elif command == "LEFT":
                col -= 1
            elif command == "UP":
                row -= 1
            else:
                row += 1
        
        return ((row * n) + col)
# @lc code=end

