# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countNodes(roots, numb):
            if not roots:
                return 0
            
            print(roots.val)
            root_valid = 0
            if roots.val >= numb:
                root_valid = 1
            
            next_val = max(numb,roots.val)
            return root_valid + countNodes(roots.right, next_val) + countNodes(roots.left,next_val)
        
        return countNodes(root, -101)
        