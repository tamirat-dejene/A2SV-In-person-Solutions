class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # tot_len - 2 * lcs
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return m + n - 2 * dp[0][0]