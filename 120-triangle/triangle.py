class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        
        for r in range(1, N):
            row = triangle[r - 1]
            triangle[r][0] += row[0]

            for c in range(1, len(row)):
                triangle[r][c] += min(row[c], row[c - 1])

            triangle[r][-1] += row[-1]
    
        return min(triangle[-1])