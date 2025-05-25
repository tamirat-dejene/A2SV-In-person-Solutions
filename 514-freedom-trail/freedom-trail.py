class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        k_sz = len(key)
        r_sz = len(ring)
        pos = defaultdict(list)
        
        for i, c in enumerate(ring):
            pos[c].append(i)

        @lru_cache(maxsize=None)
        def dfs(r_pos, k_pos):
            if k_pos >= k_sz:
                return 0

            mn_stps = float('inf')

            for ps in pos[key[k_pos]]:

                cw_stps = (ps - r_pos) % r_sz
                ccw_stps = (r_pos - ps) % r_sz

                stps = min(cw_stps, ccw_stps) + 1 + dfs(ps, k_pos + 1)

                mn_stps = min(mn_stps, stps)

            return mn_stps
                
        return dfs(0, 0)