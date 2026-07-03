#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i in count:
                return i
            else:
                count[i] = 1
# @lc code=end

