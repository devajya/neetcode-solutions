# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if not node:
                return TreeNode(val)
            if val > node.val:
                node.right = dfs(node.right, val)
            else:
                node.left = dfs(node.left, val)
            
            return node
        
        return dfs(root, value)