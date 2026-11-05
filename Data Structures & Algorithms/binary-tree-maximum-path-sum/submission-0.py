# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    res = 0

    def dfs(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        l_max = self.dfs(node.left)
        r_max = self.dfs(node.right)
        l_max = max(l_max, 0)
        r_max = max(r_max, 0)
        self.res = max(self.res, node.val + l_max + r_max)
        return node.val + max(l_max, r_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.dfs(root)
        return self.res