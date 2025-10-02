class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # recover the lcs
        i, j = 0, 0
        common = []

        while i < m and j < n:
            if str1[i] == str2[j]:
                common.append(str1[i])
                i += 1
                j += 1
            else:
                if dp[i + 1][j] >= dp[i][j + 1]:
                    common.append(str1[i])
                    i += 1
                else:
                    common.append(str2[j])
                    j += 1
            
        while i < m:
            common.append(str1[i])
            i += 1
        
        while j < n:
            common.append(str2[j])
            j += 1

        return ''.join(common)

        