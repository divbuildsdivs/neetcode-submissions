"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copymap = {}
        copymap = {None : None}

        def cloneNode(root):
            nonlocal copymap
            if root in copymap:
                return copymap[root]
            rootcopy = Node(root.val) 
            copymap[root] = rootcopy
            for neighbor in root.neighbors:
                copyneighbor = cloneNode(neighbor)
                copymap[root].neighbors.append(copyneighbor)
            return copymap[root]
        return cloneNode(node)



        
        