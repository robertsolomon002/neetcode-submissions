# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p =p.val
        q= q.val

        while root:
            rval = root.val

            if p < rval and q < rval:
                root = root.left
            if p > rval and q > rval:
                root = root.right
            
            return root
        
        return -1


        