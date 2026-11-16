class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls > lt:
            return False
        ps = 0
        pt = 0

        while pt < lt and ps < ls:
            # print("pt", pt)
            # print('t[pt]', t[pt])
            # print("ps", ps)
            # print('s[ps]', s[ps])
            if t[pt] == s[ps]:
                ps += 1
            pt += 1
            # print("ps", ps)
        return ps == ls