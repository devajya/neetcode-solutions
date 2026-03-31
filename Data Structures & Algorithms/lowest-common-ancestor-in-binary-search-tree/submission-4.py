# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = self.helper(root, p, q)
        return ans if ans else None
    def helper(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not node:
            return None
        pval = min(p.val, q.val)
        qval = max(p.val, q.val)
        if pval <= node.val and qval >= node.val:
            return node
        elif pval < node.val and qval < node.val:
            return self.helper(node.left, p, q)
        else:
            return self.helper(node.right, p, q)

        