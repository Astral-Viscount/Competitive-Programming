#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        left = 0
        
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            
            left += num
        
        return -1
# @lc code=end

