class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:

        if k < e - s or (k - (e - s)) % 2 != 0:
            return 0

        M = 10**9 + 7
        
        f = e - s
        b = (k - f) // 2
        f += b

        return (math.factorial(k) // (math.factorial(f) * math.factorial(b))) % M