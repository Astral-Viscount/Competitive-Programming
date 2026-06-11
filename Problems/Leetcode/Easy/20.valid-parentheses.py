#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for parenthese in s:
            if parenthese in parentheses:
                if stack and stack[-1] == parentheses[parenthese]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parenthese)
            
        if stack:
            return False
        else:
            return True
# @lc code=end

