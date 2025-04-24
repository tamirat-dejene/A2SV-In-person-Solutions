class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        rev = [[] for _ in range(len(graph))]

        for i, ne in enumerate(graph):
            for e in ne:
                rev[e].append(i)
                indegree[i] += 1

        queue = deque([n for n in range(len(graph)) if n not in indegree])
        res = []
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for ne in rev[curr]:
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    queue.append(ne)
        
        return sorted(res)




