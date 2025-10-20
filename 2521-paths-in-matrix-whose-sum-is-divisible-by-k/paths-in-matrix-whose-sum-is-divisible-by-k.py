class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        MOD = 1_000_000_007

        prev = [[0] * k for _ in range(N)]

        for sm in range(k):
            csm = (sm + grid[0][0]) % k
            if csm == 0:
                prev[0][sm] = 1

        for c in range(1, N):
            for sm in range(k):
                csm = (sm + grid[0][c]) % k
                prev[c][sm] = prev[c - 1][csm]

        for r in range(1, M):
            dp = [[0] * k for _ in range(N)]

            for sm in range(k):
                sm_md = (sm + grid[r][0]) % k
                dp[0][sm] = prev[0][sm_md] % MOD
            
            for c in range(1, N):
                for sm in range(k):
                    sm_md = (sm + grid[r][c]) % k

                    dp[c][sm] = (dp[c - 1][sm_md] + prev[c][sm_md]) % MOD

            prev = dp                
        
        return prev[-1][0]

        @cache
        def dfs(r, c, sm):
            if r >= M or c >= N:
                return 0

            if r == M - 1 and c == N - 1:
                return 1 if (sm + grid[r][c]) % k == 0 else 0
            
            sm_md = (sm + grid[r][c]) % k

            return (dfs(r + 1, c, sm_md) + dfs(r, c + 1, sm_md)) % MOD

        return dfs(0, 0, 0)



        