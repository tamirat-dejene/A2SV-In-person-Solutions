class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tsks = sorted([(at, pt, t) for t, [at, pt] in enumerate(tasks)])
        at, pt, t = heappop(tsks) 

        tsks_pq = [(pt, t)]
        order = []
        tm = at

        while tsks_pq:
            pt, t = heappop(tsks_pq)
            order.append(t)

            tm += pt

            while (tsks and tsks[0][0] <= tm) or (tsks and not tsks_pq):
                att, ptt, tt = heappop(tsks)
                if tsks and not tsks_pq:
                    tm = max(att, tm)
                heappush(tsks_pq, (ptt, tt))
        
        return order




