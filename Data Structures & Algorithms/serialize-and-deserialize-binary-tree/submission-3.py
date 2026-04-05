# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "N"
        ans = []
        q = [root]
        while q:
            node=q[0]
            q = q[1::]
            if node == None:
                ans.append("N")
                continue
            ans.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return " ".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(" ")
        if arr[0] == "N":
            return None
        
        ans = TreeNode(int(arr[0]))
        q = [ans]
        idx = 1
        while q:
            node = q[0]
            q = q[1::]
            # left node
            if arr[idx] != "N":
                node.left = TreeNode(int(arr[idx]))
                q.append(node.left)
            idx+=1
            # right node
            if arr[idx] != "N":
                node.right = TreeNode(int(arr[idx]))
                q.append(node.right)
            idx+=1
        return ans
            
