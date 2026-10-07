# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        visited = set()

        stack.append(root)
        while stack:
            peak = stack.pop()
            #print(peak.val)
            while peak:
                if peak.val not in visited:
                    stack.append(peak)
                    peak = peak.left
                else:
                    break
            node = stack.pop()
            if k ==1:
                return node.val
            k -=1
            visited.add(node.val)
            #print(node.val)
            #print(stack)
            if node.right:
                stack.append(node.right)
            
        