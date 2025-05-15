class UF:
    def __init__(self):
        self.root = {chr(n): chr(n) for n in range(ord('a'), ord('z') + 1)}
        self.smll = {chr(n): chr(n) for n in range(ord('a'), ord('z') + 1)}
        self.size = defaultdict(int)

    def find(self, node):
        if node == self.root[node]:
            return node

        return self.find(self.root[node])

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb: return False

        if self.size[pa] >= self.size[pb]:
            self.root[pb] = pa
            self.size[pa] += self.size[pb]
            self.smll[pa] = min(self.smll[pb], self.smll[pa]) 
        else:
            self.root[pa] = pb
            self.mn[pa] = min(self.mn[pb], b, a)
            self.size[pb] += self.size[pa]
            self.smll[pb] = min(self.smll[pb], self.smll[pa]) 
        
        return True

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UF()
        for ca, cb in zip(s1, s2):
            uf.union(ca, cb)

        return ''.join(uf.smll[uf.find(c)] for c in baseStr)
        

        

        