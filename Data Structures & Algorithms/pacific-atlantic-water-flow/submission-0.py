class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = set()
        atlantic = set()

        for j in range(len(heights[0])):
            pacific.add((0, j))
            atlantic.add((len(heights)-1, j))

        for i in range(len(heights)):
            pacific.add((i, 0))
            atlantic.add((i, len(heights[0])-1))

        def dfs(heights, i, j, ocean, visited):
            if (i<0 or j<0 or 
            i>=len(heights) or j>=len(heights[0]) or visited[i][j]):
                return

            ocean.add((i, j))
            visited[i][j] = True

            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                row = i+dr
                col = j+dc

                if (not (row<0 or col<0 or 
                    row>=len(heights) or col>=len(heights[0])) and heights[row][col] >= heights[i][j]):
                    dfs(heights, row, col, ocean, visited)
            
            return

            
        visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]

        ext_pacific = set()
        for cell in pacific:
            dfs(heights, cell[0], cell[1], ext_pacific, visited)

        pacific.update(ext_pacific)

        visited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        
        ext_atlantic = set()
        for cell in atlantic:
            dfs(heights, cell[0], cell[1], ext_atlantic, visited)

        atlantic.update(ext_atlantic)
        
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        
        return ans

