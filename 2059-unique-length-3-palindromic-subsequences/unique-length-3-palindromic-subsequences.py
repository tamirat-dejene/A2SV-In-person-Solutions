class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        srev = s[::-1]
        ans = 0

        for c in set(s):
            # c _ c
            l = s.index(c)
            r = N - srev.index(c)
            m = set()
            
            for i in range(l + 1, r - 1):
                m.add(s[i])
            
            ans += len(m)
            
        return ans




        