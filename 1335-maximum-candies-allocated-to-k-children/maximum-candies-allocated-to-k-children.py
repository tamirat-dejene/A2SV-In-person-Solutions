class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort()

        def check(cndy):
            return sum(pile // cndy for pile in candies) >= k
        
        l, r = 0, candies[-1] + 1

        while l + 1 < r:
            m = (l + r) // 2

            if check(m): l = m
            else: r = m
        
        return l
            




        