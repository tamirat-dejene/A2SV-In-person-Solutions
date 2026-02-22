class Solution:
    def binaryGap(self, n: int) -> int:


        p, ans = -1, 0
        c = 1


        while n:
            if n & 1:
                if p == -1:
                    p = c
                
                ans = max(ans, c - p)
                p = c
            
            c += 1
            n >>= 1
        
        return ans

        