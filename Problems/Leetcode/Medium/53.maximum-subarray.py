#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        total = nums[0]

        for num in nums[1:]:
            total = max(num, (total + num))
            best = max(total, best)

        return best
# @lc code=end

