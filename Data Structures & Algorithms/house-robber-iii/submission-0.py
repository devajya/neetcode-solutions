# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]

            dp[node] = node.val

            if node.left:
                dp[node] += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                dp[node] += dfs(node.right.left) + dfs(node.right.right)

            dp[node] = max(dp[node], dfs(node.left) + dfs(node.right))
            
            return dp[node]
        
        return dfs(root)