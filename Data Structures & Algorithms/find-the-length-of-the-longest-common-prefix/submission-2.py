class TrieNode:
    def __init__(self):
        self.children = {}
class NumDictionary:
    def __init__(self):
        self.root = TrieNode()
    def add(self, num):
        snum = str(num)
        curr = self.root
        for i in snum:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
    
    def match(self, num):
        snum = str(num)
        curr = self.root
        count = 0 
        for i in snum:
            if i not in curr.children:
                break
            curr = curr.children[i]
            count += 1
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        numBook = NumDictionary()
        superMax = 0
        for i in arr1:
            numBook.add(i)
    
        for i in arr2:
            currCount = numBook.match(i)
            superMax = max(superMax, currCount)
        return superMax




