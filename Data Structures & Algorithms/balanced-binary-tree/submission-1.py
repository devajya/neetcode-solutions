# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)
            
            l = dfs(node.left)
            r = dfs(node.right)

            flag = True
            if abs(l[0]-r[0]) > 1 or not l[1] or not r[1]:
                flag = False
            
            return (1+max(l[0], r[0]), flag)

        return dfs(root)[1]