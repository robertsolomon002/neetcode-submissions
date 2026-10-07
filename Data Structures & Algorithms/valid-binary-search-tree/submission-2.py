# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        comp = True
        if root.left and root.right:
            lval = root.left.val
            rval = root.right.val
            comp = lval < root.val < rval
        if not root.left and root.right:
            rval = root.right.val
            comp = root.val < rval

        if root.left and not root.right:
            lval = root.left.val
            comp = lval < root.val
        
        
        return comp and self.isValidBST(root.left) and self.isValidBST(root.right)
