#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ops =[]

        for op in operations:
            if op == "C":
                ops.pop()
            elif op == "+":
                ops.append(ops[-1] + ops[-2])
            elif op == "D":
                ops.append(ops[-1] * 2)
            else:
                ops.append(int(op))
        
        return sum(ops)ops =[]

        for op in operations:
            if op == "C":
                ops.pop()
            elif op == "+":
                ops.append(ops[-1] + ops[-2])
            elif op == "D":
                ops.append(ops[-1] * 2)
            else:
                ops.append(int(op))
        
        return sum(ops)
# @lc code=end

