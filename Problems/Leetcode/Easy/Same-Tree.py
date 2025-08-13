# https://leetcode.com/problems/same-tree/

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return str(p) == str(q)