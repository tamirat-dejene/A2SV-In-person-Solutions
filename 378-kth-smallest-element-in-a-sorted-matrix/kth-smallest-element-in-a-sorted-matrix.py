class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapify(matrix)

        while k > 1:
            
            r = heappop(matrix)
            r.pop(0)
            if r: heappush(matrix, r)

            k -= 1
        
        return heappop(matrix)[0]