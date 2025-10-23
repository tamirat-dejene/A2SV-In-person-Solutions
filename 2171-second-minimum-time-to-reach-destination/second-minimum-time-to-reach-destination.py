class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # node, time
        queue = deque([(1, 0)])

        # first and second min time to a node from 1
        fmin_t = [inf, 0] + [inf] * (n - 1)
        smin_t = [inf] * (n + 1)

        while queue:
            nd, t = queue.popleft()
            nt = t # next time

            # red interval
            if (t // change) % 2 == 1:
                nt += (t // change) * change + change - t # wait
            
            nt += time

            for ne in graph[nd]:
                if nt < fmin_t[ne]:
                    smin_t[ne] = fmin_t[ne]
                    fmin_t[ne] = nt
                    queue.append((ne, nt))
                
                elif fmin_t[ne] < nt < smin_t[ne]:
                    smin_t[ne] = nt
                    queue.append((ne, nt))

        return -1 if smin_t[n] == inf else smin_t[n]