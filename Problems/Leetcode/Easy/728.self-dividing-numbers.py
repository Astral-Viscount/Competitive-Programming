#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for i in range(left, right + 1):
            j = str(i)
            if "0" in j:
                continue 

            self_divide = True
            for k in j:
                if i % int(k) != 0:
                    self_divide = False
                    break
            
            if self_divide:
                output.append(i)
            
        return output
# @lc code=end

