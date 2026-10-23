class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        if N <= 1:
            return nums
        mid = N//2
        first = self.sortArray(nums[0:mid])
        second = self.sortArray(nums[mid:N])
        res = []
        while len(first) > 0 and len(second) > 0:
            if first[0] < second[0]:
                res.append(first.pop(0))
            else: 
                res.append(second.pop(0))
        
        if len(first) > 0:
            res.extend(first)
        elif len(second) > 0:
            res.extend(second)
        return res

        
        