"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        transform = {}

        def dfs(root):
            if not root:
                return None
            if root in transform:
                return transform[root]
            copy_root = Node(root.val)
            transform[root] = copy_root

            for n in root.neighbors:
                copy_root.neighbors.append(dfs(n))
            return copy_root


        return dfs(node)


        