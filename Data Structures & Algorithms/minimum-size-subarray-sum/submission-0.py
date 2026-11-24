class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minWindow = 0
        N = len(nums)
        window = 1
        total = nums[0]

        while l < N and r < N:
            if total < target:
                r += 1
                if r < N:
                    total += nums[r]
                window += 1 
            else:
                minWindow = window if minWindow == 0 else min(minWindow, window)
                total -= nums[l]
                l += 1
                window -= 1
        return minWindow



        