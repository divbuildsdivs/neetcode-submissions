class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def backtrack(curr, curset):
            if len(curr) == N:
                res.append(curr)
            for i in range(N):
                if nums[i] not in curset:
                    curr.append(nums[i])
                    curset.add(nums[i])
                    backtrack(curr.copy(), curset.copy())
                    curr.pop(-1)
                    curset.remove(nums[i])
        backtrack([],set())
        return res
                

        