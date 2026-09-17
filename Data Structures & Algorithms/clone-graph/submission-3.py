"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        maps = {}

        def dfs(node):
            new_node = Node(val = node.val)
            maps[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(maps[nei] if nei in maps else dfs(nei))

            return new_node

        return dfs(node) if node else None