class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [(0, [0])]
        N = len(graph)
        ans = []

        while stack:
            nd, path = stack.pop()

            if nd == N - 1:
                ans.append(path)
                continue

            for ne in graph[nd]:
                stack.append((ne, path + [ne]))
        
        return ans


        