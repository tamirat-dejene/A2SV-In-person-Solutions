class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for s, d in dislikes: 
            graph[s].append(d)
            graph[d].append(s)

        gcolor = [0] * n
        can_color = lambda clr, node: not any(gcolor[c - 1] == clr for c in graph[node])

        def dfs(node):
            for nn in graph[node]:
                if gcolor[nn - 1] != 0: continue

                for c in [1, 2]:
                    if can_color(c, nn):
                        gcolor[nn - 1] = c
                        if not dfs(nn): return False
                
                if gcolor[nn - 1] == 0: return False
                
            return True
        
        for i in range(1, n + 1):
            if gcolor[i - 1] == 0:
                gcolor[i - 1] = 1
                if not dfs(i): return False

        return True
        