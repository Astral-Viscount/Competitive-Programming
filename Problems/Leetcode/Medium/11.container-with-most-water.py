#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0,  len(height) - 1
        max_area = 0

        while left < right:
            a, b = height[left], height[right]
            y = min(a, b)
            x = right - left

            max_area = max(max_area, (x * y))
        
            if a > b:
                right -=1 
            else:
                left += 1

        return max_area
        
# @lc code=end

