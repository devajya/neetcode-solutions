class Solution:
    class DisjointSetUnion:
        def __init__(self, n):
            self.rank = [0]*(n+1)
            self.parent = list(range(n+1))
            self.num_components = n+1

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            x_root, y_root = self.find(x), self.find(y)
            if x_root == y_root:
                return False

            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[y_root] < self.rank[x_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1

            self.num_components -= 1
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = self.DisjointSetUnion(len(edges))

        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]

        return [-1, -1]
        