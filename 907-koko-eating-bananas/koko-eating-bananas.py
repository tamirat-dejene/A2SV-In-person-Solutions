class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(n):
            hr = 0

            for pile in piles:
                hr += ceil(pile / n)
            
            return hr <= h
        

        l, r = 1, max(piles)


        while l <= r:
            m = (l + r) // 2

            if valid(m): r = m - 1
            else: l = m + 1
        

        return l


        