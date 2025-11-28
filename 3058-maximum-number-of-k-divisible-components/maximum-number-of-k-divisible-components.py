class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(pr, ch): # subtree_sum, component_count
            sm, cnt = values[ch], 0
            for gc in tree[ch]:
                if gc != pr:
                    sts, stc = dfs(ch, gc)
                    sm += sts
                    cnt += stc
            
            if sm % k == 0:
                return 0, cnt + 1
            return sm, cnt

        return dfs(-1, 0)[1]
        