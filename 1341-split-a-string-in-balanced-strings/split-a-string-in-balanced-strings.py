class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt_l, cnt_r = 0, 0
        ans = 0
        
        for c in s:
            if c == 'L': cnt_l += 1
            else: cnt_r += 1

            if cnt_l == cnt_r: 
                ans += 1
                cnt_l, cnt_r = 0, 0
        
        return ans




        