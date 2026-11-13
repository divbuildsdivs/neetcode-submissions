class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [nums.pop(0) for i in range(k)]
        heapq.heapify(minheap)

        while len(nums) > 0:
            num = nums.pop(0)
            if num > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, num)
        return minheap[0]



        