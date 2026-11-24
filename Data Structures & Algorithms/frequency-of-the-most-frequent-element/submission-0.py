class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        maxWindow = 0
        N = len(nums)
        total = nums[0]

        while l < N and r < N:
            windowSize = r - l + 1
            if (nums[r] * windowSize) <= (total + k):
                maxWindow = max(maxWindow, windowSize)
                r += 1
                if r < N:
                    total += nums[r]
            else:
                total -= nums[l]
                l += 1
        return maxWindow

        