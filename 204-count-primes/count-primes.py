class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [False, False] + [True] * (n - 2)

        p = 2
        while p * p < n:
            if primes[p]:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        
        return primes.count(True)