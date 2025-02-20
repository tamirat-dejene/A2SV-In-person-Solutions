class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = min(trip[1] for trip in trips)
        dest_ = max(trip[2] for trip in trips)

        route = [0] * (dest_ - start + 1)

        for peeps, dep, dest in trips:
            route[dep - start] += peeps
            route[dest - start] -= peeps
        
        for i in range(1, len(route)):
            route[i] += route[i - 1]
        
        for peepsinbus in route:
            if peepsinbus > capacity: return False
        
        return True
        