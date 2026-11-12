class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        edgeMap = {i:[] for i in range(n)}
        edgeMap[-1] = 0
        for [x,y] in edges:
            edgeMap[x].append(y)
            edgeMap[y].append(x)

        def dfs(edge, parent):
            if edge in visited:
                return False
            visited.add(edge)
            for dep in edgeMap[edge]:
                if dep != parent and dfs(dep, edge) == False:
                    return False
            return True
        if dfs(0, -1) == False:
            return False
        return len(visited) == n

       

        