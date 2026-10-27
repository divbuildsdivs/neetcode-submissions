class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hmap = {}

        for num in nums:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
        for x, y in hmap.items():
            if y > (n/2):
                return x
        