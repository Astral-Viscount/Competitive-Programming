#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(cur_sum, node):
            if not node:
                return False

            cur_sum += node.val
            if not node.left and not node.right and cur_sum == targetSum:
                return True

            return dfs(cur_sum, node.left) or dfs(cur_sum, node.right)

        return dfs(0, root)

# @lc code=end

