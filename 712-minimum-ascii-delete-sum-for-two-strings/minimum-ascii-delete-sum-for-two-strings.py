class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # store = [[-1] * n for _ in range(m)]
        # def dfs(l, r):
        #     if l == m or r == n:
        #         return sum([0] + [ord(s1[i]) for i in range(l, m)]) + sum([0] + [ord(s2[i]) for i in range(r, n)])
            
        #     if store[l][r] == -1:
        #         if s1[l] == s2[r]:
        #             store[l][r] = dfs(l + 1, r + 1)
        #         else:
        #             store[l][r] = min(
        #                 ord(s1[l]) + dfs(l + 1, r),
        #                 ord(s2[r]) + dfs(l, r + 1)
        #             )
        #     return store[l][r]

        # return dfs(0, 0)


        # bottom up
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return sum(ord(c) for c in s1 + s2) - 2 * dp[0][0]
