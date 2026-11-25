#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]

        for i in range (numRows - 1):
            cur = [0] + result[-1] + [0]
            row = []

            for j in range(len(result[-1]) + 1):
                row.append(cur[j] + cur[j + 1])

            result.append(row)
            
        return result
# @lc code=end

