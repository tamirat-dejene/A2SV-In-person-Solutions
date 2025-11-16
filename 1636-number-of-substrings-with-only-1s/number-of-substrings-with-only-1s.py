class Solution:
    def numSub(self, s: str) -> int:
        cnt, ans = 0, 0

        for c in s:
            if c == '1':
                cnt += 1
                ans += cnt
            else:
                cnt = 0
            
        return ans % 1_000_000_007
        