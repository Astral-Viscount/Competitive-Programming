#
# @lc app=leetcode id=2535 lang=python3
#
# [2535] Difference Between Element Sum and Digit Sum of an Array
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit = 0
        for num in nums:
            while num > 0:
                digit += num % 10
                num //= 10
        return abs(sum(nums) - digit)
# @lc code=end

