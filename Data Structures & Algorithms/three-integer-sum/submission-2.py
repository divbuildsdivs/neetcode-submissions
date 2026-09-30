class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N =len(nums)
        hset = set()
        i = 0
        while i < N and nums[i] <= 0:
            if i != 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            l = i + 1
            r = N - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    hset.add(tuple(sorted([nums[i], nums[l],
                    nums[r]])))    
               
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
            i += 1
        return [ list(x) for x in hset]

