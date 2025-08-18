class UF:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * (n)
    
    def find(self, nd):
        if nd != self.root[nd]:
            self.root[nd] = self.find(self.root[nd])
        
        return self.root[nd]
    
    def union(self, nd1, nd2):
        r1 = self.find(nd1)
        r2 = self.find(nd2)

        if r1 == r2: return False

        if self.size[r1] < self.size[r2]:
            r1, r2 = r2, r1

        self.root[r2] = r1
        self.size[r1] += self.size[r2]

        return True
    
    def connected(self, nd1, nd2):
        return self.find(nd1) == self.find(nd2)

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        # Add index to queries to track original order
        queries = [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        
        # Sort edges by distance and queries by limit
        edgeList.sort(key=lambda x: x[2])
        queries.sort()
        
        # Initialize Union-Find
        uf = UF(n)
        answer = [False] * len(queries)
        edge_idx = 0
        
        # Process queries in order of increasing limit
        for limit, p, q, idx in queries:
            # Add all edges with distance < limit to Union-Find
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, _ = edgeList[edge_idx]
                uf.union(u, v)
                edge_idx += 1
            
            # Check if p and q are connected
            answer[idx] = uf.connected(p, q)
        
        return answer


                
