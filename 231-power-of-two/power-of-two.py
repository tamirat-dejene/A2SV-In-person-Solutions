class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False

        return log2(n) == int(log2(n))