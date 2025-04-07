class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for s, d in edges: 
            graph[s].append(d)
            graph[d].append(s)

        # stack = [source]
        visited = set()
        # TLEd
        # while stack:
        #     curr = stack.pop()

        #     if curr == destination: return True
        #     visited.add(curr)

        #     for d in graph[curr]:
        #         if d not in visited: stack.append(d)

        # return False


        def dfs(curr):
            if curr == destination: return True

            visited.add(curr)

            for d in graph[curr]:
                if d not in visited:
                    if dfs(d): return True
        

            return False

        
        return dfs(source)
