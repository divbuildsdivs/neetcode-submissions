class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        comparator = strs[0]
        i = 1
        n = len(comparator)
        while i < N and n > 0:
            if comparator == strs[i][:n]:
                i += 1
            else:
                comparator = strs[0][:n-1]
                n -= 1
        return comparator
        
        

        