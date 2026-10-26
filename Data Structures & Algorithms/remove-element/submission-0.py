class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        c = 1
        for i in range(N-1, -1, -1):
            if nums[i] == val:
                if i == N-1:
                    nums[i] = -1
                else:
                    nums[i] = nums[N - c]
                    nums[N-c] = -1
                c += 1
        
        return N - c + 1
                    

                