class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
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


