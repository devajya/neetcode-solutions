# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int) # (node, does_rob) -> max value obtainable

        def dfs(node):
            if not node:
                return (0, 0)
            
            a = dfs(node.left)
            b = dfs(node.right)

            withNode = node.val + a[1] + b[1]
            withoutNode = max(a)+ max(b)
            
            return (withNode, withoutNode)

        return max(dfs(root))
        
