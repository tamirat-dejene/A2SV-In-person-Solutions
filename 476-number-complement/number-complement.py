class Solution:
    def findComplement(self, num: int) -> int:
        b = []

        while num > 0:
            b.append('0' if num & 1 else '1')
            num >>= 1
        
        return int(''.join(b[::-1]), 2)
        