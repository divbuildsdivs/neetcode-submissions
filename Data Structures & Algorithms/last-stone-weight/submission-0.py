class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        N = len(stones)
        minheap =[]

        for i in range(N):
            if stones[i] == 0:
                continue
            heapq.heappush(minheap, (0 - stones[i]))
        
        while len(minheap) > 1:
            x = 0 - heapq.heappop(minheap)
            y = 0 - heapq.heappop(minheap)
            x = x - y
            if x != 0:
                heapq.heappush(minheap, 0 - x)
        if len(minheap) == 0:
            return 0
        else:
            return 0 - heapq.heappop(minheap)
        
