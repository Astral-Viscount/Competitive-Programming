#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        curr_value = n

        while curr_value != 1:
            num_list = list(str(curr_value))

            total = 0
            for i in num_list:
                total += int(i) ** 2

            if (curr_value < 4 and curr_value > 1):
                return False

            curr_value = total
            
        return True
# @lc code=end

