class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()

        def can_repair(t): 
            nonlocal cars
            return sum(int((t // r) ** 0.5) for r in ranks) >= cars

        tl = 0
        tr = ranks[-1] * (cars ** 2)


        while tl + 1 < tr:
            t = (tl + tr) // 2

            if can_repair(t):
                tr = t
            else: tl = t
        
        return tr

