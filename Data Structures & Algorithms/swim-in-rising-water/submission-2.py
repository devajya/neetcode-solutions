class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n


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
        elif self.rank[y_r] > self.rank[x_r]:
            self.parent[x_r] = y_r
        else:
            self.rank[x_r] += 1
            self.parent[y_r] = x_r

        self.num_components -= 1
        return True


    def are_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cells = sorted((grid[i][j], i, j) for i in range(n) for j in range(n))
        uf = UnionFind(n*n)

        for h, r, c in cells:
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = r+dx, c+dy
                if 0<=nx<n and 0<=ny<n:
                    if grid[nx][ny] < h:
                        uf.union(r*n + c, nx*n + ny)
            if uf.are_connected(0, n*n-1):
                return h
