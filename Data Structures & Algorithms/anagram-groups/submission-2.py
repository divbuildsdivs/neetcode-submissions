class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}
        for str in strs:
            freqArray = [0] * 26
            for ch in str:
                index = ord(ch) - ord('a')
                freqArray[index] += 1

            freqTuple = tuple(freqArray)
            if freqTuple not in groupMap:
                groupMap[freqTuple] = []
            groupMap[freqTuple].append(str)

        res = [ vals for vals in groupMap.values()]
        return res