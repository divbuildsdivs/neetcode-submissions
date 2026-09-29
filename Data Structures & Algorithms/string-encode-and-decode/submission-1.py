class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + "#"+s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        print(s)
        while i < len(s):
            print(s[i])
            c = i
            numstr = ""
            while s[c] != "#":
                numstr += s[c] 
                c += 1
            n = int(numstr)
            start = c+1
            end = start + n
            st = s[start : end]
            res.append(st)
            i = end

        return res
        
            
