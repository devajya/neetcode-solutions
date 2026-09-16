"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(i, j, n):
            if n == 1:
                return Node(
                    grid[i][j],
                    True
                )
            
            mid = n//2
            tl = dfs(i, j, mid)
            tr = dfs(i, j+mid, mid)
            bl = dfs(i+mid, j, mid)
            br = dfs(i+mid, j+mid, mid)


            are_leaves = tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
            are_same = tl.val == tr.val == bl.val == br.val

            if are_leaves and are_same:
                return Node(
                    tl.val,
                    True
                )

            return Node(
                False,
                False,
                tl,
                tr,
                bl,
                br
            )       


        return dfs(0,0,len(grid))     

