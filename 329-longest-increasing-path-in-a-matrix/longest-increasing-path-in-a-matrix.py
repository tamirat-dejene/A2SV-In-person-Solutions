class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        def neigh(r, c):
            return [
                (a, b) for a, b in [
                    (r + 1, c),
                    (r, c + 1),
                    (r - 1, c),
                    (r, c - 1)
                ] if 0 <= a < m and 0 <= b < n
            ]

        mn_r, mn_c = 0, 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] < matrix[mn_r][mn_c]:
                    mn_r, mn_c = r, c
                

        def dfs(r, c):
            if dp[r][c] != -1: 
                return dp[r][c]

            for nr, nc in neigh(r, c):
                if matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(1 + dfs(nr, nc), dp[r][c])
            
            dp[r][c] = max(dp[r][c], 1)
            
            return dp[r][c]

        ans = 1    
        for r in range(m):
            for c in range(n):
                if dp[r][c] == -1:
                    dfs(r, c)
                ans = max(ans, dp[r][c])
  
        return ans