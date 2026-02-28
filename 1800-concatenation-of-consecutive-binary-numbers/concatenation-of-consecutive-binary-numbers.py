class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        ans = 0

        for num in range(1, n + 1):
            ans <<= num.bit_length()
            ans |= num
            ans %= 1_000_000_007
        
        return ans
