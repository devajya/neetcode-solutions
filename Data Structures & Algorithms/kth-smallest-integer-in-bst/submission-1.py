# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inOrder(root, arr):
            if not root:
                return
            
            inOrder(root.left, arr)
            arr.append(root.val)
            inOrder(root.right, arr)
        inOrder(root, arr)
        return arr[k-1]