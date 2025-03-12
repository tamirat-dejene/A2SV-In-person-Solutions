class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def nthbin(n, b="0"):
            if n == 1: return b
            prev = nthbin(n - 1)
            inverted = ''.join(['0' if k == '1' else '1' for k in prev])
            return prev + "1" + inverted[::-1]
        
        return nthbin(n)[k-1]