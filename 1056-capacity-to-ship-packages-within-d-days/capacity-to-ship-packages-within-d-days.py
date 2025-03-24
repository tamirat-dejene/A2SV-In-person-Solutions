class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def ispossible(cap):
            cnt, sm = 0, 0
            
            for weigh in weights:
                sm += weigh
                if sm > cap: 
                    cnt += 1
                    sm = weigh

            return cnt + 1 <= days
        

        l, r = max(weights), sum(weights)

        while l <= r:
            m = (l + r) // 2

            if ispossible(m): r = m - 1
            else: l = m + 1
        
        return l