class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        ''' text1: abcde, text2: ace
                0   1   2   3   4
                a   b   c   d   e
        0   a --|       |       |
                        |       |
        1   c ----------|       |
                                |
        2   e ------------------|
        '''
        dp = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if text1[j] == text2[i]:
                    curr[j] = 1 + dp[j + 1]
                else:
                    curr[j] = max(dp[j], curr[j + 1])
            
            dp = curr

        return dp[0]

        # Top Down
        store = [[-1]*n for _ in range(m)]
        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if store[i][j] == -1:
                if text1[i] == text2[j]:
                    store[i][j] = 1 + dfs(i + 1, j + 1)
                else:
                    store[i][j] = max(dfs(i, j + 1), dfs(i + 1, j))
            
            return store[i][j]

        return dfs(0, 0)