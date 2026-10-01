# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = [root.val]

        def largest_at_node(root):
            if not root:
                return 0
            
            value_root = root.val

            left_child = largest_at_node(root.left)
            left_child = max(0, left_child)

            right_child = max(0, largest_at_node(root.right))

            result[0] = max(result[0], value_root + left_child + right_child)

            return value_root + max(left_child,right_child)

        largest_at_node(root)
        return result[0]


        