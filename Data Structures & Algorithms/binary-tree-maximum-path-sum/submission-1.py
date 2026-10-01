# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize global maximum path sum to a very small value
        res = [float('-inf')]  # This will store the global maximum
        
        # Helper function to perform DFS
        def dfs(root):
            if not root:
                return 0  # Return 0 for null nodes, since they don't add to the path

            # Recursively get the maximum sum from the left and right subtrees
            left_max = max(dfs(root.left), 0)  # Ignore negative paths
            right_max = max(dfs(root.right), 0)  # Ignore negative paths

            # Calculate the path sum including the current node + left + right
            max_end = root.val + left_max + right_max

            # Update the global result with the maximum path sum found
            res[0] = max(res[0], max_end)

            # Return the maximum path sum for the current node to its parent
            return root.val + max(left_max, right_max)

        # Start DFS
        dfs(root)
        
        # Return the final global maximum path sum
        return res[0]


        