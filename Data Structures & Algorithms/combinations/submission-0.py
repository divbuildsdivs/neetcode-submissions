class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(index, curr):
            nonlocal k, res, n
            if len(curr) == k:
                res.append(curr)
            else:
                for i in range (index, n+1):
                    curr.append(i)
                    dfs(i + 1, curr.copy())
                    curr.pop(-1)
            
        dfs(1, [])
        return res


        