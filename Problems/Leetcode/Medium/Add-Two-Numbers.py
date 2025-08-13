# https://leetcode.com/problems/add-two-numbers/
#
#  @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return list(str(int("".join([str(num) for num in reversed(list(l1))])) + int("".join([str(num) for num in reversed(list(l2))])))[::-1])
# @lc code=end

