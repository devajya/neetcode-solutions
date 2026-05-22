class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(board, i, j):
            if (i<0 or j<0 or i>=n or j>=m 
                or board[i][j] == "X" or board[i][j] == "T"):
                return
            
            board[i][j] = "T"

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(board, i+dr, j+dc)
            
            return

        for i in range(0, n):
            dfs(board, i, 0)
            dfs(board, i, m-1)

        
        for j in range(0, m):
            dfs(board, 0, j)
            dfs(board, n-1, j)


        print(board)

        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
                

        return
                