class DSU:
    def __init__(self, n):
        self.rank = [1]*n
        self.parent = list(range(n))
        self.num_comp = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_r, y_r = self.find(x), self.find(y)
        if x_r == y_r:
            return False
        
        if self.rank[x_r] > self.rank[y_r]:
            self.parent[y_r] = x_r
        if self.rank[y_r] > self.rank[x_r]:
            self.parent[x_r] = y_r
        else:
            self.parent[y_r] = x_r
            self.rank[x_r] += 1
        self.num_comp-=1

        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DSU(n)

        for x, y in edges:
            uf.union(x, y)
        
        return uf.num_comp