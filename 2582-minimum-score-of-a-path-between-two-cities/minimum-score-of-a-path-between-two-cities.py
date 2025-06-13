
class UF:
    def __init__(self, sz):
        self.root = [n for n in range(sz + 1)]
        self.size = [1] * (sz + 1)
    
    def find(self, nd):
        while nd != self.root[nd]:
            self.root[nd] = self.root[self.root[nd]]
            nd = self.root[nd]  
        
        return nd

    def union(self, nd1, nd2):
        rt1 = self.find(nd1)
        rt2 = self.find(nd2)

        if rt1 == rt2: return False

        if self.size[rt1] >= self.size[rt2]:
            self.root[rt2] = rt1
            self.size[rt1] += self.size[rt2]
        else:
            self.root[rt1] = rt2
            self.size[rt2] += self.size[rt1]

        return True

    def connected(self, nd1, nd2):
        return self.find(nd1) == self.find(nd2)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key=lambda itm: itm[2])
        print(roads)
        mn = float('inf')
        uf = UF(n)

        for a, b, ln in roads:
            if not uf.connected(a, b):
                uf.union(a, b)
        
        for a, b, ln in roads:
            if uf.find(1) == uf.find(a):
                mn = min(mn, ln)

        return mn


        