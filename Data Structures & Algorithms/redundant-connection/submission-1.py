class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(1, len(edges)+1)}
        rank = [1] * (len(parent) + 1)

        def findParent(p):
            while p != parent[p]:
                p = parent[parent[p]]
            return p
        def merge(p1, p2):
            par1 = findParent(p1)
            par2 = findParent(p2)

            if par1 == par2:
                return False
            else:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                    rank[par1] += 1
                else:
                    parent[par1] = par2
                    rank[par2] += 1
            return True
        for edge in edges:
            if not merge(edge[0], edge[1]):
                return edge
        