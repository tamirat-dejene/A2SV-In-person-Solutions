
class UF:
    def __init__(self, sz):
        self.size = [1] * (sz)
        self.root = [n for n in range(sz)]
    
    def find(self, nd):
        if nd != self.root[nd]:
            self.root[nd] = self.find(self.root[nd])
        
        return self.root[nd]

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UF(len(s))
        for pa, pb in pairs:
            uf.union(pa, pb)
        
        grp = defaultdict(SortedList)

        for idx in range(len(s)):
            grp[uf.find(idx)].add(s[idx])
        
        ptr = {r:0 for r in grp}

        res = []

        for idx in range(len(s)):
            rt = uf.find(idx)
            res.append(grp[rt][ptr[rt]])
            ptr[rt] += 1
        
        return ''.join(res)
        
        