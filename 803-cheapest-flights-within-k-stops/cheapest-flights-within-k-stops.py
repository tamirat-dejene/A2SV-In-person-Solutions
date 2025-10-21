class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = [inf] * n
        prev[src] = 0

        for _ in range(k + 1): 
            tmp = prev[:]
            for u, v, cost in flights:
                if tmp[u] != inf and tmp[u] + cost < prev[v]:
                    prev[v] = tmp[u] + cost

        return prev[dst] if prev[dst] != inf else -1
