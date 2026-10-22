class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        def dfs(r, c):
            nonlocal perimeter
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dir in dirs:
                x = r + dir[0]
                y = c + dir[1]
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = -1
                        dfs(x, y) 
                elif 0 <= x < rows and 0 <= y < cols and grid[x][y] == -1:
                    continue
                else:
                    perimeter += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    dfs(i, j)
                    return perimeter
                