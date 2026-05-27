#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        
        while right > left:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1    
        
        return left
# @lc code=end

