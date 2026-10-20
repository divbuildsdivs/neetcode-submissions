class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def checkSum(curr, start):
            if sum(curr) == target:
                res.append(curr)
                return
            elif sum(curr) > target:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                checkSum(curr.copy(), i)
                curr.pop()
        checkSum([], 0)
        return res        