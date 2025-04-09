class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for r in range(n): 
            for c in range(n):
                if isConnected[r][c]:
                    graph[r].append(c)
        
        visited = set()
        
        def dfs(c):
            for ne in graph[c]:
                if ne not in visited:
                    visited.add(ne)
                    dfs(ne)
        
        cnt = 0
        for r in range(n):
            if r not in visited:
                dfs(r)
                cnt += 1
        
        return cnt

