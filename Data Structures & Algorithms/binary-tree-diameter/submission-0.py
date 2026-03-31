# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = self.helper(root)
        print(ans)
        return ans[0]
    def helper(self, node: Optional[TreeNode]) -> List[int]:
        # [a, b] a is max diameter so far, b is max len so far
        if not node:
            return [0, 0]
        
        left = self.helper(node.right)
        left_di, left_mlen = left[0], left[1]
        right = self.helper(node.left)
        right_di, right_mlen = right[0], right[1]

        max_di = max(left_mlen + right_mlen , max(left_di, right_di))
        max_len = max(left_mlen+1, right_mlen+1)

        return [max_di, max_len]
    