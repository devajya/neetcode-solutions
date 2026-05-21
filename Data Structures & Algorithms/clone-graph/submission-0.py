"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}

        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            new_copy = Node(node.val)
            mapping[node] = new_copy
            for n in node.neighbors:
                new_copy.neighbors.append(dfs(n))
            return new_copy

        return dfs(node)

    
    