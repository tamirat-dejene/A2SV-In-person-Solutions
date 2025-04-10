class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for e in range(n):
            m, it = manager[e], informTime[e]
            if m == -1: continue
            graph[m].append((e, it))

        ans = informTime[headID]

        def dfs(emp, t):
            nonlocal ans
            ans = max(ans, t)

            for e, it in graph[emp]:
                dfs(e, t + it)

        dfs(headID, ans)

        return ans