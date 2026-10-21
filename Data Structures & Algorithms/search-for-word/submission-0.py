class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(index, r, c, visited):
            if index == len(word):
                return True
            visited.add((r,c))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dir in dirs:
                x = r + dir[0]
                y = c + dir[1]
                
                if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited and board[x][y] == word[index]:
                    if backtrack(index + 1, x, y, visited.copy()):
                        return True
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = set()
                    if backtrack(1, i, j, visited):
                        return True
        
        return False

        