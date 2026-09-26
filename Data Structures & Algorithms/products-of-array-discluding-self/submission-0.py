class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prodleft = [1] * N
        prodright = [1] * N
        res = []
        
        for i in range(1, N):
            prodleft[i] = prodleft[i - 1] * nums[i-1]
            prodright[N-1-i] = prodright[N-i] * nums[N-i]
        for i in range(N):
            res.append(prodleft[i] * prodright[i])
        return res
