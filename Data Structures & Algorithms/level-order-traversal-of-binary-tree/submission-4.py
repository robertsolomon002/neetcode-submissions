# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()

        queue.append(root)
        res = []
        row = []

        while queue:
            len_q = len(queue)

            for _ in range(len_q):
                node = queue.popleft()

                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(row)
            row = []

        return res


        