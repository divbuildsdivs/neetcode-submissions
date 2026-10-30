class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen = len(s)
        tlen = len(t)
        if tlen > slen or t == "":
            return ""
        tmap = {}
        smap = {}
        minSubString = ""
        for i in range(tlen):
            self.addCharToMap(t[i], tmap)
        need = len(tmap)
        have = 0
        l = 0
        r = -1
        while r < slen:
            if have != need:
                r += 1
                if r < slen and s[r] in tmap:
                    self.addCharToMap(s[r], smap)
                    if smap[s[r]] == tmap[s[r]]:
                        have += 1
                
            else:
                if minSubString == "" or len(minSubString) >= r+1-l:
                    minSubString = s[l:r+1]
                if s[l] in smap:
                    self.removeCharFromMap(s[l], smap)
                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1

        return minSubString


    def addCharToMap(self, ch, chmap):
            if ch not in chmap:
                chmap[ch] = 0
            chmap[ch] += 1

    def removeCharFromMap(self, ch, chmap):
            chmap[ch] -= 1
        
        