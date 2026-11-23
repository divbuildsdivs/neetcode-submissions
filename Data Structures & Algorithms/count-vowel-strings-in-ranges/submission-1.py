class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hset = set(["a", "e", "i", "o", "u"])
        hmap = { }
        res = []
    
        if words[0][0] in hset and words[0][-1] in hset:
            hmap[0] = 1
        else:
            hmap[0] = 0
        for i in range(1, len(words)):
            if words[i][0] in hset and words[i][-1] in hset:
                hmap[i] = hmap[i-1] + 1
            else:
                hmap[i] = hmap[i-1]
        

        for i in range(len(queries)):
            x = queries[i][0]
            y = queries[i][1]
            if x == 0:
                res.append(hmap[y])
            else:
                res.append(hmap[y] - hmap[x - 1])
        return res