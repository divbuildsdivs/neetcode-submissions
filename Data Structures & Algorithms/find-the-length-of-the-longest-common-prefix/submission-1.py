class TrieNode:
    def __init__(self):
        self.children = {}
    def add(self, num):
        snum = str(num)
        curr = self
        for i in snum:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
    
    def match(self, num):
        snum = str(num)
        curr = self
        count = 0 
        for i in snum:
            if i not in curr.children:
                break
            curr = curr.children[i]
            count += 1
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trieNode = TrieNode()
        superMax = 0
        for i in arr1:
            trieNode.add(i)
    
        for i in arr2:
            currCount = trieNode.match(i)
            superMax = max(superMax, currCount)
        return superMax




