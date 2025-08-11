class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []

        for l, r in queries:
            nc, p = n, 0
            i, pos = 0, 0
            
            while l <= r:
                if nc & 1:
                    if i == l:
                        p += pos
                        l += 1
                    i += 1
                
                nc >>= 1  
                pos += 1

            res.append((1 << p) % (10**9 + 7))

        return res

