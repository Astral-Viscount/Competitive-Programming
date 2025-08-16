#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        best = 0
        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            if sell > buy:
                new = sell - buy
                best = max(best, new)
            else:
                left = right
            right += 1
        
        return best
            
# @lc code=end

