# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        self.helper(root, float("-infinity"), count)
        return count[0]
        
    def helper(self, node: TreeNode, max_n: int, count: List[int]) -> None:
        if not node:
            return

        if node.val >= max_n:
            count[0]+=1
        
        max_n = max(node.val, max_n)
        self.helper(node.left, max_n, count)
        self.helper(node.right, max_n, count)

        return
        