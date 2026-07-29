#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for j in range(len(temperatures)):
            temp = temperatures[j]
            count = 0
            for i in range(j, len(temperatures)):
                if temperatures[i] > temp:
                    count = i - j
                    break
            
            res.append(count)
        
        return res
# @lc code=end

