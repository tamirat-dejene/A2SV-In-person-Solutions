class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda itm: abs(itm[0] - itm[1]), reverse=True) # process max cost diff first

        ans, ca, cb = 0, 0, 0
        tot = len(costs) // 2

        for a, b in costs:
            if a <= b:
                if ca < tot:
                    ca += 1
                    ans += a
                else:
                    cb += 1
                    ans += b
            else:
                if cb < tot:
                    cb += 1
                    ans += b
                else:
                    ca += 1
                    ans += a
        return ans
