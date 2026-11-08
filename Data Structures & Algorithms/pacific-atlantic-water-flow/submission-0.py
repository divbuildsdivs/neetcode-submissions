class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        pacifics = set()
        atlantics = set()
        res = []

        def dfs(r, c, ocean):
            nonlocal heights
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dir in dirs:
                x = r + dir[0]
                y = c + dir[1]
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in ocean and heights[x][y] >= heights[r][c]: 
                    ocean.add((x, y))
                    dfs(x, y, ocean)
        
        for i in range(rows):
            pacifics.add((i, 0))
            dfs(i, 0, pacifics)
            atlantics.add((i, cols - 1))
            dfs(i, cols - 1, atlantics)
        for i in range(cols):
            pacifics.add((0, i))
            dfs(0, i, pacifics)
            atlantics.add((rows - 1, i))
            dfs(rows - 1, i, atlantics)
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacifics and (i, j) in atlantics:
                    res.append([i, j])
        
        return res


        