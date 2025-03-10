class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = defaultdict(int)
        ncpy, n = n, abs(n)
        
        def p(x, n):
            if n == 1: return x
            if n == 0: return 1

            a = memo.get(n // 2) if (n // 2) in memo else p(x, n // 2)
            b = memo.get((n // 2) + (n % 2)) if (n // 2) + (n % 2) in memo else p(x, (n // 2) + (n % 2))

            memo[n // 2] = a
            memo[(n // 2) + (n % 2)] = b

            return a * b

        ans = p(x, n)

        return ans if ncpy  >= 0 else (1 / ans)
            

            





        