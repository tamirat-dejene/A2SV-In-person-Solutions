class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        visited = set()
        
        def dfs(node):
            ecnt = 0
            ncnt = 1

            for ne in graph[node]:
                if ne not in visited:
                    visited.add(ne)
                    nc, ec = dfs(ne)
                    ncnt += nc
                    ecnt += ec

            return [ncnt, ecnt + len(graph[node])]
        
        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                nc, ec = dfs(i)

                if nc * (nc - 1) == ec:
                    res += 1

        return res



        