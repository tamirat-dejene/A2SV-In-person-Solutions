class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        cnt1, cnt2 = num1.bit_count(), num2.bit_count()
        ans = num1
        
        if cnt1 < cnt2: 
            # turn on the least significant 0 bits
            pos = 0
            while cnt2 - cnt1 > 0:
                if not num1 & 1:
                    ans |= (1 << pos)
                    cnt1 += 1
                
                num1 >>= 1
                pos += 1
        
        elif cnt1 > cnt2:
            # turn off the least significant 1 bits
            pos = 0
            while cnt1 - cnt2 > 0:
                if num1 & 1:
                    ans &= ((1 << 31) - 1) ^ (1 << pos)
                    cnt1 -= 1
                
                num1 >>= 1
                pos += 1


        return ans