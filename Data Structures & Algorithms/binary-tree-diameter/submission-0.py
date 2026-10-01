# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        
        self.diameter = 0
        
        # Helper function to calculate height and update the diameter
        def height(node):
            if not node:
                return 0
            
            # Recursively find the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # The diameter at this node is the sum of the left and right subtree heights
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        # Call the helper function on the root
        height(root)
        
        return self.diameter

        