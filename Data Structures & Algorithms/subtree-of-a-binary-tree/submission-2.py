# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False
        
        if self.dfs(root, subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
    
    def dfs(self, node, subnode):
            if not node and not subnode:
                return True
            if not node and subnode or not subnode and node:
                return False
            if node.val != subnode.val:
                return False
            
            l = self.dfs(node.left, subnode.left)
            r = self.dfs(node.right, subnode.right)

            if l and r and node.val == subnode.val:
                return True
            
            return False



