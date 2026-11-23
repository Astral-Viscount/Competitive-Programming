#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(arr, n):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] > n:
                    right = mid - 1
                elif arr[mid] < n:
                    left = mid + 1
                else:
                    return mid
            
            return -1
        
        return binary_search(nums, target)
# @lc code=end

