# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        maps = {val:i for i, val in enumerate(inorder)}
        preorder_idx = 0
        
        
        def dfs(start, end):
            nonlocal preorder_idx
            if start > end:
                return None
            
            root_val = preorder[preorder_idx]
            node = TreeNode(root_val)
            preorder_idx += 1

            inorder_idx = maps[root_val]

            node.left = dfs(start, inorder_idx-1)
            node.right = dfs(inorder_idx+1, end)

            return node

        return dfs(0, len(inorder)-1)