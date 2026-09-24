class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        minHeap = []
        for i in range(len(nums)):
            if nums[i] not in freqmap:
                freqmap[nums[i]] = 0
            freqmap[nums[i]] += 1

        for x, y in freqmap.items():
            minHeap.append([y,x])
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        res = [x[1] for x in minHeap]
        return res
