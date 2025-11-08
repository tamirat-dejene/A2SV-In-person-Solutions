class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(pnd, cnd):
            tot = 0
            got_one = hasApple[cnd]

            for gcnd in tree[cnd]:
                if gcnd == pnd: continue

                h, t = dfs(cnd, gcnd)
                got_one = h or got_one
                tot += 2 * h + t
                    
            return got_one, tot

        
        return dfs(-1, 0)[1]
        