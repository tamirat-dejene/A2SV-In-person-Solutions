class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * N
        dp[-1] = questions[-1][0]

        for i in range(N - 2, -1, -1):
            p, l = questions[i]
            dp[i] = max(dp[i + 1], p + (dp[i + l + 1] if i + l + 1 < N else 0))
        
        return dp[0]

        store = [-1] * N
        def dfs(idx):
            if idx >= N:
                return 0
            
            if store[idx] == -1:
                store[idx] = max(questions[idx][0] + dfs(idx + questions[idx][1] + 1), dfs(idx + 1))
            
            return store[idx]
        
        return dfs(0)
        