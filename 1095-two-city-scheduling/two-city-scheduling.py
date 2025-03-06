class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: -abs(cost[0] - cost[1]))
        a, b, lim = 0, 0, len(costs) // 2
        tot_cost = 0

        for ca, cb in costs:
            if (ca <= cb and a < lim) or b >= lim:
                tot_cost += ca
                a += 1
            else:
                tot_cost += cb
                b += 1
        
        return tot_cost




        

        