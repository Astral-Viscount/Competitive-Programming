#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay, need = len(haystack), len(needle)

        for i in range(hay - need + 1):
            if haystack[i:i + need] == needle:
                return i
        
        return -1
# @lc code=end

