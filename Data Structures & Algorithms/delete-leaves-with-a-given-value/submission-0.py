# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                node.left = None
            if right:
                node.right = None
            
            if left and right and node.val == target:
                return True
            
            return False
        
        dfs(root)
        return root if root.val != target else None