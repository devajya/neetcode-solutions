# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = self.helper(root)
        print(ans)
        return ans
        
    def helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        right = self.helper(node.right)
        left = self.helper(node.left)

        return max(right+1, left+1)