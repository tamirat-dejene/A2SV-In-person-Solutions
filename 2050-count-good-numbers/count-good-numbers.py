class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        e = n // 2 + n % 2
        o = n - e

        return pow(5, e, m) * pow(4, o, m) % m
        
        res = 1

        for i in range(64):
            if e & 1:
                res *= int(pow(5, 1 << i))
            if o & 1:
                res *= int(pow(4, 1 << i))

            e >>= 1
            o >>= 1
            res %= m
        
        return res