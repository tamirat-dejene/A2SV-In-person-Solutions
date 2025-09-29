class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            elif l == r:
                return 1
            
            if s[l] == s[r]:
                return 2 + dfs(l + 1, r - 1)
            else:
                return max(dfs(l + 1, r), dfs(l, r - 1))

        return dfs(0, len(s) - 1)





