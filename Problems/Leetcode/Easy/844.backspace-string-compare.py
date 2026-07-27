#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_new = []
        t_new = []

        for char in s:
            if char == "#":
                if s_new:
                    s_new.pop()
                continue

            s_new.append(char)
        
        for char in t:
            if char == "#":
                if t_new:
                    t_new.pop()
                continue

            t_new.append(char)
        
        if len(s_new) != len(t_new):
            return False
        
        for i in range(min(len(s_new), len(t_new))):
            if s_new[i] != t_new[i]:
                return False
        
        return True
# @lc code=end

