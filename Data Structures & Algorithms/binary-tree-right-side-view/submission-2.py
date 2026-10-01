# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_side = []
        q = deque()
        q.append(root)

        while q:
            dLen = len(q)

            latest = None

            for i in range(dLen):
                node = q.popleft()

                if node:
                    latest = node
                    q.append(node.left)
                    q.append(node.right)
            

            if latest:
                right_side.append(latest.val)
        return right_side