# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        levels = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            l = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if l:
                levels.append(l)
        
        return [l[-1] for l in levels]