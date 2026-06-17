#
# @lc app=leetcode id=3232 lang=python3
#
# [3232] Find if Digit Game Can Be Won
#

# @lc code=start
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for i in nums:
            if i <= 9:
                single += i
            else:
                double += i
        
        return single != double
        # return (sum([i for i in nums if i <= 9]) != sum([k for k in nums if  k > 9]))
# @lc code=end

