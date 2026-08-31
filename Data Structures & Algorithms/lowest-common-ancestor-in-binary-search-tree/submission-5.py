# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        LOWER_BOUND = -101
        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)

            if l is not None and r is not None:
                return node
            elif l is not None:
                return l
            elif r is not None:
                return r
            
            return None

        return dfs(root)
            

