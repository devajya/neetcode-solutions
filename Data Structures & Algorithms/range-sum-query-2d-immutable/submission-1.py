class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.grid_sums = [[0 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                top = self.getSum(i - 1, j)
                left = self.getSum(i, j - 1)
                top_left = self.getSum(i - 1, j - 1)
                
                self.grid_sums[i][j] = matrix[i][j] + top + left - top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole = self.getSum(row2, col2)
        above = self.getSum(row1 - 1, col2)
        behind = self.getSum(row2, col1 - 1)
        corner = self.getSum(row1 - 1, col1 - 1)

        return whole - above - behind + corner

    def getSum(self, x: int, y: int) -> int:
        if x < 0 or y < 0:
            return 0
        return self.grid_sums[x][y]