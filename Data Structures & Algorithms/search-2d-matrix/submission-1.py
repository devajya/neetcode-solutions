class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row to search in, terminate early if no row is suitable
        up, down = 0, len(matrix)-1
        row = -1
        while up <= down:
            row = (up+down)//2
            if target > matrix[row][-1]:
                up=row+1
            elif target < matrix[row][0]:
                down= row-1
            else:
                break
        

        left, right = 0, len(matrix[row])-1
        while left <= right:
            col = (left+right) // 2
            if target > matrix[row][col]:
                left = col+1
            elif target < matrix[row][col]:
                right= col-1
            else:
                return True

        return False