class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hmap = {}
        minheap = []
        res =[]

        for [x, y] in points:
            distance = math.sqrt(x**2 + y**2)
            minheap.append(distance)
            if distance not in hmap:
                hmap[distance] = []
            hmap[distance].append([x, y])
        heapq.heapify(minheap)

        while len(res) < k:
            dis = heapq.heappop(minheap)
            res.append(hmap[dis].pop(0))
        return res

