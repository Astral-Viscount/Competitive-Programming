#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                j = stack.pop()
                i = stack.pop()

                if token == "+":
                    stack.append(i + j)
                elif token == "-":
                    stack.append(i - j)
                elif token == "*":
                    stack.append(i * j)
                elif token == "/":
                    stack.append(int(i / j))
            else:
                stack.append(int(token))
        
        return stack.pop()
# @lc code=end

