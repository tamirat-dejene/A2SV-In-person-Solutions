class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            a, b = edges[i]
            w = inf if succProb[i] == 0 else 1 / succProb[i]

            graph[a].append((b, w))
            graph[b].append((a, w))

        distances = [inf] * n
        hp = [(1, start_node)]
        parent = {start_node: -1}

        while hp:
            d, nd = heappop(hp)

            for ne, w in graph[nd]:
                dis = d * w

                if dis < distances[ne]:
                    parent[ne] = (nd, w)
                    distances[ne] = dis
                    heappush(hp, (dis, ne))
        

        ans = 1
        curr = end_node

        while curr != start_node:
            if curr not in parent:
                return 0
            par, w = parent[curr]

            if w == inf:
                return 0
            ans *= (1 / w)
            curr = par

        return ans


        