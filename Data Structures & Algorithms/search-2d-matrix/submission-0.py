class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        r = m*n - 1

        while l <= r:
            mid = int((l + r)//2)
            row = int(mid // n)
            col = int(mid % n)
            print(row, col)
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        return False