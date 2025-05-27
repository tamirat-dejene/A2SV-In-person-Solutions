class Solution:
    def find(self, nd, root):
        if nd != root[nd]:
            root[nd] = self.find(root[nd], root)  
        return root[nd]
    
    def union(self, nd1, nd2, root, size):
        rt1 = self.find(nd1, root)
        rt2 = self.find(nd2, root)

        if rt1 == rt2: return False

        if size[rt2] > size[rt2]:
            rt1, rt2 = rt2, rt1
        
        root[rt2] = rt1
        size[rt1] += size[rt2]

        return True

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        ln = len(source)
        root = list(range(ln))
        size = [1] * ln

        for pi, pj in allowedSwaps:
            self.union(pi, pj, root, size)
        
        sstore = defaultdict(list)
        tstore = defaultdict(list)
        
        for nd in range(ln):
            pr = self.find(nd, root)
            sstore[pr].append(source[nd])
            tstore[pr].append(target[nd])

        ans = 0
        for i in sstore:
            cnts = Counter(sstore[i])
            cntt = Counter(tstore[i])
            
            ans += len(sstore[i]) - sum(min(cnts[c], cntt[c]) for c in cnts)
            
        return ans