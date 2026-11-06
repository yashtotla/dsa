from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        return self._clone(node, {})
    
    def _clone(self, node, lookup):
        if node in lookup:
            return lookup[node]
        copy = Node(node.val)
        lookup[node] = copy

        for ne in node.neighbors:
            copy.neighbors.append(self._clone(ne, lookup))
        
        return copy
