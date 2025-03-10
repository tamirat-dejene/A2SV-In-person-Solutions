class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def div_4(n):
            if n == 1: return True
            if n % 4 != 0 or n < 1: return False
            return div_4(n / 4)


        
        return div_4(n)

