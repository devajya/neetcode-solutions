import random
class Solution:
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
      return None

    if key > root.val:
      root.right = self.deleteNode(root.right, key)
    elif key < root.val:
      root.left = self.deleteNode(root.left, key)
    else:
      if not root.left:
        return root.right
      if not root.right:
        return root.left

      # Case with 2 children: Randomly pick predecessor or successor
      use_successor = random.choice([True, False])

      if use_successor:
        # Successor: Smallest in right subtree
        cur = root.right
        while cur.left:
          cur = cur.left
        root.val = cur.val
        root.right = self.deleteNode(root.right, root.val)
      else:
        # Predecessor: Largest in left subtree
        cur = root.left
        while cur.right:
          cur = cur.right
        root.val = cur.val
        root.left = self.deleteNode(root.left, root.val)

    return root