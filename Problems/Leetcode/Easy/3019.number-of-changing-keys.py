#
# @lc app=leetcode id=3019 lang=python3
#
# [3019] Number of Changing Keys
#

# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                count += 1
        
        return count
# @lc code=end

