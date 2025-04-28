class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(set)
        indeg = defaultdict(int)
        for a, b in enumerate(edges):
            if b != -1:
                graph[a].add(b)
                indeg[b] += 1
        
        non_cycle = set()
        queue = deque([n for n in range(len(edges)) if n not in indeg])

        while queue:
            node = queue.popleft()
            non_cycle.add(node)

            for ne in graph[node]:
                indeg[ne] -= 1

                if indeg[ne] == 0:
                    queue.append(ne)
        
        cycle = [n for n in range(len(edges)) if n not in non_cycle]
        visited = set()
        ans = -1

        for c in cycle:
            if c not in visited:
                indeg[c] = 0
                visited.add(c)
                queue = deque([(c, 1)])

                while queue:
                    node, ln = queue.popleft()

                    for ne in graph[node]:
                        if indeg[ne] == 0:
                            ans = max(ans, ln)
                            continue
                        indeg[ne] -= 1
                        queue.append((ne, ln + 1))
                        visited.add(ne)
        return ans
                    
        



        

        
        