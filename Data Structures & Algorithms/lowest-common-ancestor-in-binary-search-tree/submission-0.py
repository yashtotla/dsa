# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    la = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val <= q.val or p.val > root.val > q.val:
            return root
        self.la = root
        if p.val < root.val and q.val < root.val:
            self.la = root.left
            self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            self.la = root.right
            self.lowestCommonAncestor(root.right, p, q)
        return self.la