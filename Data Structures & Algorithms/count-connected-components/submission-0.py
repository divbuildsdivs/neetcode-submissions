class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        hmap = {i: [] for i in range(n)}
        count = 0
        for [x, y] in edges:
            hmap[x].append(y)
            hmap[y].append(x)
        

        def dfs(node):
            visited.add(node)
            for dep in hmap[node]:
                if dep not in visited:
                    dfs(dep)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count


        