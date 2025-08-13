# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while left_pointer < right_pointer:
            two_sum = numbers[left_pointer] + numbers[right_pointer]

            if two_sum > target:
                right_pointer -= 1
            elif two_sum < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]
            