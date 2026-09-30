class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        hmap = {}
        hset = set()
        
        for i in range(N):
            if nums[i] not in hmap:
                hmap[nums[i]] = 0
            hmap[nums[i]] += 1
        
        i = 0 
        while i < N and nums[i] <= 0:
            if i != 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            for j in range(i+1, N):
                target = 0 - (nums[i] + nums[j])
                
                if target not in hmap:
                    continue
                
                if (target == nums[i] and target == nums[j]) and hmap[target] <= 2:
                    continue
                
                if (target == nums[i] or target == nums[j]) and hmap[target] <= 1:
                    continue
                hset.add(tuple(sorted([nums[i], nums[j], target])))
            i += 1
        
        res = [list(el) for el in hset]
        return res