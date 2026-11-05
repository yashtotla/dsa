# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        levels = []
        q = [root]
        i = 0

        while i < len(q):
            lsize = len(q) - i
            l = []

            for _ in range(0, lsize):
                node = q[i]
                i += 1

                l.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            levels.append(l)
        
        return levels