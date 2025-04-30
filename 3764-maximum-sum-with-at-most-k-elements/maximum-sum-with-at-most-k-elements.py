class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        mod = [(sorted(map(lambda itm: -itm, row)), i) for i, row in enumerate(grid) if limits[i] > 0]
        heapify(mod)

        sm = 0
        
        while k > 0:
            row, i = heappop(mod)

            sm -= heappop(row)
            limits[i] -= 1

            if row and limits[i] > 0:
                heappush(mod, (row, i))
            
            k -= 1

        return sm


        