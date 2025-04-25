class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for p, c in prerequisites:
            graph[p].append(c)
            indeg[c] += 1

        queue = deque([i for i in range(numCourses) if i not in indeg])
        pre = defaultdict(set)

        while queue:
            curr = queue.popleft()
            
            for ne in graph[curr]:  
                indeg[ne] -= 1
                pre[ne].update(pre[curr])
                pre[ne].add(curr)

                if indeg[ne] == 0:
                    queue.append(ne) 
            
        return [p in pre[c] for p, c in queries]
        