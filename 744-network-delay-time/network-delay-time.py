class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, t in times:
            graph[s].append((d, t))
        
        mint = [float('+inf')] * n
        mint[k - 1] = 0

        stack = [(k, 0)]

        while stack:
            node, c = stack.pop()

            for ne, tm in graph[node]:
                if c + tm >= mint[ne - 1]: continue
                mint[ne - 1] = c + tm
                stack.append((ne, c + tm))

        ans = max(mint)

        return ans if ans != float('inf') else -1
        

        

        