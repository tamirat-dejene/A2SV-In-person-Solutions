class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        store = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i == m or j == n:
                for k in range(j, n):
                    if p[k] != '*' and (k + 1 == n or p[k + 1] != '*'):
                        return False
        
                return i == m

            if store[i][j] == -1:
                if j + 1 < n and p[j + 1] == '*':
                    k = i

                    while k < m and (s[k] == p[j] or p[j] == '.'):
                        if dfs(k, j + 2):
                            store[i][j] = True
                            break
                        
                        k += 1

                    if store[i][j] == -1:
                        store[i][j] = dfs(k, j + 2)

                else:
                    store[i][j] = (s[i] == p[j] or p[j] == '.') and dfs(i + 1, j + 1)

            return store[i][j]

        return dfs(0, 0)