# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]
    def helper(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            # 0 index is sum, 1 index is path
            return [float("-infinity"),0]            
        
        left = self.helper(node.left)
        l_max_sum, l_max_path = left[0], left[1]

        right = self.helper(node.right)
        r_max_sum, r_max_path = right[0], right[1]

        temp_max_sum = l_max_path + r_max_path + node.val
        tot_max_sum = max(temp_max_sum, l_max_sum, r_max_sum)

        temp_max_path = max(0, l_max_path, r_max_path) + node.val
        tot_max_path =  temp_max_path if temp_max_path > 0 else 0

        print(node.val)
        print("lms, lmp", l_max_sum, l_max_path)
        print("rms, rmp", r_max_sum, r_max_path)
        print("tempms, tempmp", temp_max_sum, temp_max_path)
        print("tms, tmp", tot_max_sum, tot_max_path)

        return [tot_max_sum, tot_max_path]
