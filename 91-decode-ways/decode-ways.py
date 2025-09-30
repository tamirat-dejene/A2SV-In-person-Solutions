class Solution:
    def numDecodings(self, s: str) -> int:
        store = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            if store[i] == -1:
                store[i] = 0
                for j in range(i, min(i + 2, len(s))):
                    if 1 <= int(s[i:j + 1]) <= 26:
                        store[i] += dfs(j + 1)
                
            return store[i]

        return dfs(0)