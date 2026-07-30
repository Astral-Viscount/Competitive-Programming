#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []
        
        for i in range(len(temperatures)):
            while mono_stack and temperatures[i] > temperatures[mono_stack[-1]]:
                idx = mono_stack.pop()
                res[idx] = i - idx
            
            mono_stack.append(i)
        
        return res

# @lc code=end

