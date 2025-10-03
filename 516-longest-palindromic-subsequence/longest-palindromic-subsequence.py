
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0]*N for _ in range(N)]


        for l in range(N - 1, -1, -1):
            dp[l][l] = 1
            for r in range(l + 1, N):
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l + 1][r - 1]
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        
        return dp[0][-1]

        # memo = [[-1] * len(s) for _ in range(len(s))]
        
        # def dfs(l, r):
        #     if l > r:
        #         return 0
        #     elif l == r:
        #         return 1

        #     if memo[l][r] != -1:
        #         return memo[l][r]
            
            
        #     if s[l] == s[r]:
        #         memo[l][r] = 2 + dfs(l + 1, r - 1)
        #     else:
        #         memo[l][r] = max(dfs(l + 1, r), dfs(l, r - 1))
            
        #     return memo[l][r]

        # return dfs(0, len(s) - 1)


















