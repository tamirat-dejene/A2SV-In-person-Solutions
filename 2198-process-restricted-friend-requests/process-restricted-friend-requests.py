
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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UF(n)
        res = []

        for a, b in requests:
            pa = uf.find(a)
            pb = uf.find(b)

            possible = True

            for ra, rb in restrictions:
                pra, prb = uf.find(ra), uf.find(rb)

                if (pra, prb) == (pa, pb) or (pra, prb) == (pb, pa):
                    possible = False
                    break
            
            if possible:
                uf.union(a, b)
            
            res.append(possible)
        
        return res
                


            



        
        
