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

        seen = {}
        # (original node, copied node)
        def copy(node: Optional['Node']) -> Optional['Node']:
            if node in seen:
                return seen[node]
            
            copied = Node(node.val)
            seen[node] = copied

            for nei in node.neighbors:
                if nei in seen:
                    n = seen[nei]
                else:
                    n = copy(nei)

                copied.neighbors.append(n)
            
            return copied
        
        copy(node)
        return seen[node]
                
