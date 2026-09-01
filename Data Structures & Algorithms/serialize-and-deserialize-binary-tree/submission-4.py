# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"
        
        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
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
        idx = 1

        q = deque([ans])
        while q:
            node = q.popleft()
            if arr[idx] != "N":
                node.left = TreeNode(int(arr[idx]))
                q.append(node.left)
            
            idx += 1

            if arr[idx] != "N":
                node.right = TreeNode(int(arr[idx]))
                q.append(node.right)
            
            idx += 1
        
        return ans


        
