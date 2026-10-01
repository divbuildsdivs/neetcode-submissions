class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        finalMax = 0
        l = 0
        r = 0
        hset = set()
        while l < N and r < N:
            if s[r] not in hset:
                hset.add(s[r])
                r += 1
            else:
                finalMax = max(finalMax, len(hset))
                hset.remove(s[l])
                l += 1
        finalMax = max(finalMax, len(hset))
        return finalMax

             