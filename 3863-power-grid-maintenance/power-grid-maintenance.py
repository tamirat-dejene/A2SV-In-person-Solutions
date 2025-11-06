class UF:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
    
    def find(self, nd):
        if self.root[nd] != nd:
            self.root[nd] = self.find(self.root[nd])
        
        return self.root[nd]

    def union(self, nd1, nd2):
        p1 = self.find(nd1)
        p2 = self.find(nd2)

        if p1 == p2:
            return False
        
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        
        self.root[p2] = p1
        self.size[p1] += self.size[p2]

        return True
    
    def connected(self, nd1, nd2):
        return self.find(nd1) == self.find(nd2)
    

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UF(c)

        for a, b in connections:
            uf.union(a, b)

        store = defaultdict(list)
        for s in range(1, c + 1):
            p = uf.find(s)
            heappush(store[p], s)
        
        onn = [True] * (c + 1)
            
        ans = []
        for cmd, s in queries:

            if cmd == 1:
                if onn[s]:
                    ans.append(s)
                else:
                    hp = store[uf.find(s)]
                    while hp and not onn[hp[0]]:
                        heappop(hp)
                    
                    if not hp:
                        ans.append(-1)
                    else:
                        ans.append(hp[0])
            else:
                onn[s] = False


        return ans
        