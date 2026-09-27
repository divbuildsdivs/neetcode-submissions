class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        hset = set(nums)
        maxim = 1
        i = 0
        while i < N:
            seq = 1
            if nums[i] - 1 not in hset:
                num = nums[i] + 1
                while num in hset:
                    seq += 1
                    num += 1
                    maxim = max(seq, maxim)
            i += 1


        return maxim
            
                
        
            
