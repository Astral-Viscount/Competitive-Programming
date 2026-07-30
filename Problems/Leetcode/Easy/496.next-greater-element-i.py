#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {}
        stack = []
        res = []

        for num in nums2:
            while stack and num > stack[-1]:
                nums1_num = stack.pop()
                greater[nums1_num] = num
            
            stack.append(num)
        
        for i in nums1:
            res.append(greater.get(i, -1))
        
        return res
# @lc code=end

