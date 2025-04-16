class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for rs, re in redEdges:
            graph[rs].append((re, 'R'))
        for bs, be in blueEdges:
            graph[bs].append((be, 'B'))
        
        ans = [-1] * n

        queue = deque([(0, '', 0)])
        visited = set([(0, '')])

        while queue:
            nd, col, dis = queue.popleft()
            ans[nd] = dis if ans[nd] == -1 else ans[nd]

            for nn, ec in graph[nd]:
                if (nn, ec) not in visited and ec != col:
                    visited.add((nn, ec))
                    queue.append((nn, ec, dis + 1))
                   
        return ans