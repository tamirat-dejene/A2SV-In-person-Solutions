class UF:
    def __init__(self, size):
        self.root = [n for n in range(size + 1)]
        self.size = [1 for _ in range(size + 1)]

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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        hp = []
        for t, a, b in edges:
            heappush(hp, (-t, a, b))
        
        ufa = UF(n)
        ufb = UF(n)

        ea, eb, cnt = 0, 0, 0

        while hp:
            if ea >= n - 1 and eb >= n - 1:
                break
                
            t, nd1, nd2 = heappop(hp)

            if t == -3:
                a = ufa.union(nd1, nd2) 
                b = ufb.union(nd1, nd2) 
                
                cnt += (1 if a or b else 0)
                ea += (1 if a else 0)
                eb += (1 if b else 0)

            elif t == -2:
                if ufb.union(nd1, nd2):
                    cnt += 1
                    eb += 1
            else:
                if ufa.union(nd1, nd2):
                    cnt += 1
                    ea += 1
        
        return len(edges) - cnt if (ea >= n - 1 and eb >= n - 1) else -1