class Solution:
    def solveNQueens(self, n: int):
        ans = []

        def update_sights(i, j, seen_by, val):
            for r in range(n):
                for c in range(n):
                    if (
                        r == i or
                        c == j or
                        r - c == i - j or
                        r + c == i + j
                    ):
                        seen_by[r][c] += val

        def backtrack(row, seen_by, curr_soln):
            if row == n:
                ans.append(["".join(r) for r in curr_soln])
                return

            for col in range(n):
                if seen_by[row][col] == 0:

                    curr_soln[row][col] = 'Q'
                    update_sights(row, col, seen_by, 1)

                    backtrack(row + 1, seen_by, curr_soln)

                    curr_soln[row][col] = '.'
                    update_sights(row, col, seen_by, -1)

        seen_by = [[0] * n for _ in range(n)]
        curr_soln = [['.'] * n for _ in range(n)]

        backtrack(0, seen_by, curr_soln)

        return ans