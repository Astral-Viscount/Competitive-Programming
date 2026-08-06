#
# @lc app=leetcode id=3345 lang=python3
#
# [3345] Smallest Divisible Digit Product I
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            new = [int(j) for j in str(n)]
            
            total = 1
            for i in new:
                total *= i

            if total % t == 0:
                return n

            n += 1
# @lc code=end

