class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dir in dirs:
                x = r + dir[0]
                y = c + dir[1]

                if 0 <= x < rows and  0 <= y < cols and grid[x][y] == "1":
                    grid[x][y] = "-1"
                    dfs(x, y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
        
        