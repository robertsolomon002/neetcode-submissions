# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            dLen = len(q)
            local = []

            for i in range(dLen):
                node = q.popleft()
                if node:
                    local.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if local:
                res.append(local)
        return res