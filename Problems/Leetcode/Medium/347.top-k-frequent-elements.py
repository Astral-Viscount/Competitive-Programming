#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        output = []
        for num in nums:
            values[i] = values.get(num, 0) + 1
        values = sorted(values.items(), key=lambda item: item[1], reverse=True)
        for j in range(k):
            output.append(values[j][0])
        return output
# @lc code=end

