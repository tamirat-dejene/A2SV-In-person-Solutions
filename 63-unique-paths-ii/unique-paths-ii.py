class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        ways = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    ways[r][c] = 0
                elif r == 0 and c == 0:
                    ways[r][c] = 1 - obstacleGrid[0][0]
                elif r == 0:
                    ways[r][c] += ways[r][c - 1]
                elif c == 0:
                    ways[r][c] += ways[r - 1][c]
                else:
                    ways[r][c] = ways[r - 1][c] + ways[r][c - 1]
        
        return ways[m-1][n-1]