class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        def dfs(curr, start):
            res.append(curr)
            for i in range(start, N):
                curr.append(nums[i])
                dfs(curr.copy(), i+1)
                curr.pop()
        dfs([], 0)
        return res
            

        