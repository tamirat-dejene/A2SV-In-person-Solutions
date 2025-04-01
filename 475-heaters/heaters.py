class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        def issufficient(rad, hs=0, ht=0):
            if hs >= len(houses): return True
            if ht >= len(heaters): return False

            while hs < len(houses):
                if houses[hs] < heaters[ht] - rad: return False
                elif houses[hs] > heaters[ht] + rad: return issufficient(rad, hs, ht + 1)
                hs += 1
            
            return True

        mn, mx = -1, max(heaters[-1], houses[-1])

        while mn + 1 < mx:
            r = (mn + mx) // 2
            if issufficient(r): mx = r
            else: mn = r
        
        return mx

        