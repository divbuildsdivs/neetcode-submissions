class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = defaultdict(int)
        tmap = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 1
            if t[i] not in tmap:
                tmap[t[i]] = 1
            smap[s[i]] += 1
            tmap[t[i]] += 1
        
        for i in range(len(s)):
            if smap[s[i]] != tmap[s[i]] or smap[t[i]] != tmap[t[i]]:
                return False
        return True
