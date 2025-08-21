#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        output = []
        for permutation in itertools.permutations(nums):
            output.append(permutation)
        return output
# @lc code=end

