class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[p].append(c)
        
        indegree = defaultdict(int)
        
        visited = set()

        def dfs(p):
            for c in graph[p]:
                indegree[c] += 1
                if c not in visited:
                    visited.add(c)
                    dfs(c)
        
        for c in range(numCourses):
            if c not in visited:
                visited.add(c)
                dfs(c)

        queue = deque([n for n in range(numCourses) if n not in indegree])
        res = []

        while queue:
            curr = queue.popleft()
            res.append(curr)

            for ne in graph[curr]:
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    queue.append(ne)
        
        return res if len(res) == numCourses else []
        



        