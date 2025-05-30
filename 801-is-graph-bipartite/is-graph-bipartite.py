class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        gcolor = [0] * n
        can_color = lambda clr, node: not any(gcolor[c] == clr for c in graph[node])

        def dfs(node):
            for nn in graph[node]:
                if gcolor[nn] != 0: continue

                for c in [1, 2]:
                    if can_color(c, nn):
                        gcolor[nn] = c
                        if not dfs(nn): return False
                
                if gcolor[nn] == 0: return False
                    
            return True
        
        for i in range(n):
            if gcolor[i] == 0:
                gcolor[i] = 1
                if not dfs(i): return False
        
        return True




