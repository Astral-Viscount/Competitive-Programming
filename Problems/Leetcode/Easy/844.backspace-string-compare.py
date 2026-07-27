#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            
            i -= 1
            j -= 1
        
        return True

        # s_new = []
        # t_new = []

        # for char in s:
        #     if char == "#":
        #         if s_new:
        #             s_new.pop()
        #         continue

        #     s_new.append(char)
        
        # for char in t:
        #     if char == "#":
        #         if t_new:
        #             t_new.pop()
        #         continue

        #     t_new.append(char)
        
        # return s_new == t_new
        
        # if len(s_new) != len(t_new):
        #     return False
        
        # for i in range(min(len(s_new), len(t_new))):
        #     if s_new[i] != t_new[i]:
        #         return False
        
        # return True
# @lc code=end

