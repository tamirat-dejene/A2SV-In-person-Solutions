class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        frds = [(a, d, f) for f, [a, d] in enumerate(times)]
        frds.sort()

        seat = list(range(len(times)))
        heap = []

        for a, d, f in frds:
            while heap and heap[0][0] <= a:
                _, s = heappop(heap)
                heappush(seat, s)
            
            st = heappop(seat)

            if f == targetFriend:
                return st
            heappush(heap, (d, st))

        
            
            

            



        