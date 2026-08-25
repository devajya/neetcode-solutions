class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1]*n
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
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
        else:
            self.rank[x_root] += 1
            self.parent[y_root] = x_root
        
        self.num_components -= 1
        return True
    
    def are_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # get the cells and contents
        n = len(grid)
        cells = []
        for i in range(n):
            for j in range(n):
                cells.append((grid[i][j], i, j))

        # order by height
        cells = sorted(cells, key = lambda x: x[0])
        uf = UnionFind(n*n)

        for h, r, c in cells:
            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr, nc = r+dx, c+dy
                if 0<=nr<n and 0<=nc<n:
                    if grid[nr][nc] < grid[r][c]:
                        uf.union(r*n+c, nr*n+nc)
            if uf.are_connected(0, n*n-1):
                return h
        


        
