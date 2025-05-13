class UF:
    def __init__(self, size):
        self.root = [n for n in range(size)]
        self.size = [1 for _ in range(size)]

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb: return False

        if self.size[pa] >= self.size[pb]:
            self.root[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.root[pa] = pb
            self.size[pb] += self.size[pa]
        
        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        sz = len(strs)
        uf = UF(sz)

        for i in range(sz):
            for j in range(sz):
                if i == j: continue

                pi = uf.find(i)
                pj = uf.find(j)

                if pi == pj: continue

                stri = strs[i]
                strj = strs[j]
                diff = 0

                for ci, cj in zip(stri, strj):
                    if ci != cj:
                        diff += 1
                    if diff > 2: break
                
                if diff <= 2:
                    uf.union(i, j)
    
        return len(set(Counter(uf.root)))