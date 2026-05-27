#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:

            mid = (right + left) // 2
            num = guess(mid)

            if num == 0:
                return mid
            elif num == -1:
                right = mid
            else:
                left = mid + 1
        
# @lc code=end

