class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        hmap = {}
        
        for i in range(N):
            if nums[i] not in hmap:
                hmap[nums[i]] = 0
            hmap[nums[i]] += 1
        x = 0
        j = 0
        for i in range(3):
            if i not in hmap:
                continue
            x += hmap[i]
            while j < x:
                nums[j] = i
                j += 1
            