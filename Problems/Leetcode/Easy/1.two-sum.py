# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, j in enumerate(nums):
            second_num = target - j

            if second_num in values:
                return [i, values[second_num]]
                
            values[j] = i