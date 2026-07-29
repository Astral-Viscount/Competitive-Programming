#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []

        def backtracking(i):
            result.append(cur.copy()) 
            
            for i in range(i, len(nums)):
                cur.append(nums[i])
                backtracking(i + 1)
                cur.pop()

        backtracking(0)

        return result

        # result = []
        # cur = []

        # def backtracking(i, result, cur, nums):
        #     if i >= len(nums):
        #         result.append(cur.copy())
        #         return
            
        #     for i in range(i, len(nums)):
        #         cur.append(nums[i])
        #         backtracking(i + 1, result, cur, nums)
        #         cur.pop()

        # return result

# @lc code=end

