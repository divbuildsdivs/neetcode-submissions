class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr, index):
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False

                elif word[i] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[i]]
            return curr.isEnd
        return dfs(curr, 0)

        
