# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(root, low, top):
            if not root:
                return True

            if not (low < root.val < top):
                return False

            return checkValid(root.right, root.val, top) and checkValid(root.left, low, root.val)


        
        return checkValid(root, -1001, 1001)
        