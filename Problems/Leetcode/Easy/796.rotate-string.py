#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s == goal:
                return True
                exit()
            else:
                s += s[0]
                s = s[1:]
        return False
# @lc code=end

