class Solution:
    def maxOperations(self, s: str) -> int:


        cnt = 0
        N = len(s)
        p = -1
        ans = 0

        for i in range(N):
            if (p != '1' and s[i] == '1') or (s[i] == '0' and i == N - 1):
                ans += cnt

            cnt += (1 if s[i] == '1' else 0)
            p = s[i]

        return ans

        