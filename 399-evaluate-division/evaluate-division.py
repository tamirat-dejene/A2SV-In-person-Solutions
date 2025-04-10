class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, [a, b] in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))


        def dfs(a, b, visited, prod=1):
            if a == b and graph[a] and graph[b]: return prod

            for bi, val in graph[a]:
                if bi not in visited:
                    visited.add(bi)
                    ans = dfs(bi, b, visited, prod * val)
                    if ans != -1: return ans
            
            return -1

        
        return [dfs(a, b, set([a])) for a, b in queries]
        