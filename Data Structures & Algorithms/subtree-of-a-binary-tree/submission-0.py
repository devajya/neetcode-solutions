# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = self.helper(root, subRoot)
        return ans
    
    def helper(self, node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
        if not subNode:
            return True
        
        if not node:
            return False
        
        if self.sameTree(node, subNode):
            return True
        
        return (self.helper(node.left, subNode)) or (self.helper(node.right, subNode))
    
    def sameTree(self, node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
        if not node and not subNode:
            return True
        if node and subNode and node.val == subNode.val:
            return (self.sameTree(node.left, subNode.left)) and (self.sameTree(node.right, subNode.right))
        return False



        