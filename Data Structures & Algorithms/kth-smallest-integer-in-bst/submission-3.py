# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        peak = root

        while stack or peak:

            while peak:

                stack.append(peak)
                peak = peak.left



            node = stack.pop()

            if k ==1:
                return node.val
            k -=1

            peak = node.right
            
        