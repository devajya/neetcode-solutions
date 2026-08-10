# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        q = deque([root])
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                elem = q.popleft()
                
                if elem.left:
                    q.append(elem.left)

                if elem.right:
                    q.append(elem.right)
                
                level.append(elem.val)
            ans.append(level)
        return ans

                
