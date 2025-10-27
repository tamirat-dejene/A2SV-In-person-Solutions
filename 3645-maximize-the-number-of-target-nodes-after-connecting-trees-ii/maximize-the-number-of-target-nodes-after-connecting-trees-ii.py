class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        M, N = len(edges1) + 1, len(edges2) + 1
        t1, t2 = [[] for _ in range(M)], [[] for _ in range(N)]

        for a, b in edges1:
            t1[a].append(b)
            t1[b].append(a)
        
        for a, b in edges2:
            t2[a].append(b)
            t2[b].append(a)

        
        def dfs(tree):
            ans = [[], []]
            
            stack = [(0, 0)]
            vis = set([0])

            while stack:
                nd, lvl = stack.pop()
                ans[lvl % 2].append(nd)

                for ne in tree[nd]:
                    if ne not in vis:
                        vis.add(ne)
                        stack.append((ne, lvl + 1))

            return ans
        
        g1 = dfs(t1)
        g2 = dfs(t2)
        more = max(len(g2[0]), len(g2[1]))

        el, ol = len(g1[0]), len(g1[1])

        ans = [0] * M

        for e in g1[0]:
            ans[e] = el + more
        
        for o in g1[1]:
            ans[o] = ol + more
        
        return ans