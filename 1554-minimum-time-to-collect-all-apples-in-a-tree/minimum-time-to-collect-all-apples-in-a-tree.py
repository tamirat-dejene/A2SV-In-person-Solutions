class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        store = {}

        def dfs(pnd, cnd):
            tot = 0
            got_one = hasApple[cnd]

            for gcnd in tree[cnd]:
                if gcnd == pnd: continue

                h = dfs(cnd, gcnd)
                tot += 2 * h
                got_one = h or got_one
                    
            store[cnd] = tot
            return got_one

        
        dfs(-1, 0)
        return  sum(store.values())
        