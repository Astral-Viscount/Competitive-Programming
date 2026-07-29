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

        def backtracking(i, result, cur, nums):
            if i >= len(nums):
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtracking(i + 1, result, cur, nums)
            cur.pop()

            backtracking(i + 1, result, cur, nums)

        backtracking(0, result, cur, nums)

        return result

# @lc code=end

