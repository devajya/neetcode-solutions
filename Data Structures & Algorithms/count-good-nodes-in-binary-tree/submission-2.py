# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_max):
            if not node:
                return 0
            
            val = 1 if node.val >= cur_max else 0
            new_max = max(node.val, cur_max)
            return val + dfs(node.right, new_max) + dfs(node.left, new_max)
            

        return dfs(root, float("-inf"))