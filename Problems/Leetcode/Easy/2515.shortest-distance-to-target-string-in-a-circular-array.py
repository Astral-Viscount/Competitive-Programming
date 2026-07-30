#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        best = float('inf')

        for i in range(len(words)):
            if words[i] == target:
                best =  min(min(abs((i - startIndex)), (len(words) - abs(i - startIndex))), best)
        
        if best != float('inf'):
            return best
        else:
            return -1
# @lc code=end

