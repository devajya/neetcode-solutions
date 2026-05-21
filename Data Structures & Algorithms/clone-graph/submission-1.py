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
        
        mapping = {} # maps node to its copy
        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            copy = Node(node.val)
            mapping[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        dfs(node)

        return mapping[node]