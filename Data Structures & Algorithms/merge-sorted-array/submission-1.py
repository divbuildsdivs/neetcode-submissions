class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        r1 = m-1 
        r2 = n - 1
        for i in range(n + m - 1, -1, -1): 
            print('r1', r1, 'r2', r2)
            if r1 < 0 or (r2 >= 0 and nums2[r2] >= nums1[r1]):
                nums1[i] = nums2[r2]
                r2 -= 1
            else:
                nums1[i] = nums1[r1]
                r1 -= 1
            print(i, nums1)
           