class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        
        for r in range(1, N):
            triangle[r][0] += triangle[r - 1][0]

            for c in range(1, len(triangle[r - 1])):
                triangle[r][c] += min(triangle[r - 1][c], triangle[r - 1][c - 1])

            triangle[r][-1] += triangle[r - 1][-1]
    
        return min(triangle[-1])