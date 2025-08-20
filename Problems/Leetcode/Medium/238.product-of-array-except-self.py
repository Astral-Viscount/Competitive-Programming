#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            new = nums.copy()
            del new[i]
            product = 1
            for n in new:
                product *= n
            output.append(product)
        return output
# @lc code=end

