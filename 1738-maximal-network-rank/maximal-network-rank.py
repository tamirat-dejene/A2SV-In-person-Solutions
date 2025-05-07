
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        deg = [0] * n
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
            deg[a] += 1
            deg[b] += 1
        
        ans = 0
        for a in range(n): 
            for b in range(a + 1, n):
                ans = max(ans, deg[a] + deg[b] - (1 if a in graph[b] or b in graph[a] else 0))

        return ans
