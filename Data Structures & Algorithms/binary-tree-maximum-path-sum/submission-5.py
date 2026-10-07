# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            left_opt = max(0,dfs(node.left))
            right_opt = max(0, dfs(node.right))

            result[0] = max(result[0], node.val +left_opt +right_opt)

            return node.val + max(left_opt, right_opt)


        



        dfs(root)
        return result[0]



