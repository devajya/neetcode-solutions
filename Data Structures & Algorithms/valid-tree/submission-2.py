class Solution:
    class DisjointSetUnion():
        def __init__(self, n):
            self.rank= [0]*n
            self.parent = list(range(n))
            self.num_components = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            x_root = self.find(x)
            y_root = self.find(y)

            if x_root == y_root:
                return False

            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1
            
            self.num_components-=1
            return True


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = self.DisjointSetUnion(n)
        for x, y in edges:
            if dsu.find(x) == dsu.find(y):
                return False
            dsu.union(x, y)
        
        return dsu.num_components == 1

