class Solution:
    def countHomogenous(self, s: str) -> int:
        p = ''
        p, cnt, ans = '', 0, 0

        for c in s:
            if p == c or p == '':
                cnt += 1
            else:
                cnt = 1
            
            ans += cnt
            p = c

        return ans % 1_000_000_007