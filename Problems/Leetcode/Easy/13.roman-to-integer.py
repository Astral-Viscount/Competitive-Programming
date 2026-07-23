#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        num = 0

        for i in range(len(s) - 1):
            first = values[s[i]]
            second = values[s[i + 1]]
            
            if second > first:
                num -= first
            else:
                num += first

        num += values[s[-1]]

        return num
# @lc code=end

