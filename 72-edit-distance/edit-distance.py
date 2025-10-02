class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if word1[i] == word2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # return max(len(word1) - dp[0][0], len(word2) - dp[0][0], 0)
        
        store = [[-1] * n for _ in range(m)]

        def dfs(l, r):
            if l == m or r == n:
                return max(m - l, n - r)

            if store[l][r] == -1:
                if word1[l] == word2[r]:
                    store[l][r] = min(1 + dfs(l + 1, r), dfs(l + 1, r + 1))
                else:
                    store[l][r] = min(
                        dfs(l, r + 1), # insert
                        dfs(l + 1, r), # delete,
                        dfs(l + 1, r + 1) # replace
                    ) + 1
            
            return store[l][r]
            
        return dfs(0, 0)
        