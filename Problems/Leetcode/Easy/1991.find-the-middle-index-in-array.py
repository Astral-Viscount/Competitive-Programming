#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        left = 0
        
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            
            left += num
        
        return -1
# @lc code=end

