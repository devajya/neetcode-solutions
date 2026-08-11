# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if node is None:
                return 0

            val = 1 if cur_max <= node.val else 0
            n_max = max(node.val, cur_max)
            return val + dfs(node.left, n_max) + dfs(node.right, n_max)
        
        return dfs(root, float("-inf"))