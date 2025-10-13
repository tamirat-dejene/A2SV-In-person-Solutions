class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N = len(s)
        tree = [[] for _ in range(N)]
        idx = defaultdict(list) # char: [IDX]
        res = [1] * N

        for nd in range(1, len(s)):
            tree[parent[nd]].append(nd)
        
        def dfs(par):
            idx[s[par]].append(par)
            
            for i in range(len(tree[par])):
                c = tree[par][i]
                if c == -1: continue

                dfs(c)
                
                if idx[s[c]]:
                    tree[idx[s[c]][-1]].append(c)
                    tree[par][i] = -1
            
            idx[s[par]].pop()

        def dfs2(nd):
            for ch in tree[nd]:
                if ch != -1:
                    res[nd] += dfs2(ch)
            return res[nd]
        
        dfs(0) # adjust
        dfs2(0) # count

        return res