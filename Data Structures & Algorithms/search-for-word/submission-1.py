class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        def backtrack(curr_string, i, j, visited):
            if curr_string == word:
                return True
            if (i<0 or j<0 or 
                i>=len(board) or j>=len(board[0]) or
                visited[i][j] or len(curr_string) > len(word)):
                return False
            
            visited[i][j] = True
            if(backtrack(curr_string+board[i][j], i+1, j, visited) or 
                backtrack(curr_string+board[i][j], i, j+1, visited) or 
                backtrack(curr_string+board[i][j], i-1, j, visited) or 
                backtrack(curr_string+board[i][j], i, j-1, visited)):
                    return True

            visited[i][j] = False
            return False

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if backtrack("", i, j, visited):
                    return True
        return False