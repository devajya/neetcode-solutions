# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = defaultdict(int) # (node, does_rob) -> max value obtainable

        def dfs(node, can_rob):
            if not node:
                return 0
            
            if (node, can_rob) in dp:
                return dp[(node, can_rob)]
            
            a = node.val + dfs(node.left, False) + dfs(node.right, False) if can_rob else 0
            b = dfs(node.left, True) + dfs(node.right, True)
            
            dp[(node, can_rob)] = max(a, b)

            return dp[node, can_rob]

        return dfs(root, True)
        
