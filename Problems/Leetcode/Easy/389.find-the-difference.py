#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if i not in s or t.count(i) != s.count(i):
                return i


# @lc code=end

