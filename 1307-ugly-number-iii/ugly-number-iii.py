class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab, lcm_ac, lcm_bc, lcm_abc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)
        
        check = lambda k: n <= k // a + k // b + k // c - k // lcm_ab - k // lcm_bc - k // lcm_ac + k // lcm_abc

        l, r = 0, 2*10**9 + 1

        while l + 1 < r:
            m = (l + r) // 2

            if check(m):
                r = m
            else:
                l = m
        return r