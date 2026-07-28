#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return (nums.pop(nums.index(max(nums))) - 1) * (nums.pop(nums.index(max(nums))) - 1)

        # nums.sort()
        # return (nums[-1] - 1) * (nums[-2] - 1)
# @lc code=end

