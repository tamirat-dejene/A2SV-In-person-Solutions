class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, e in edges: graph[s].append(e)

        odg = defaultdict(int)
        idg = defaultdict(int)
        visited = set()
        
        def dfs(node):
            for ne in graph[node]:
                odg[node] += 1
                idg[ne] += 1
                if ne not in visited:
                    visited.add(ne)
                    dfs(ne)
            
        for t in range(n):
            if t not in visited:
                dfs(t)

        ans = [k for k in range(n) if idg[k] == 0]
        
        return -1 if not ans or len(ans) >= 2 else ans[-1]