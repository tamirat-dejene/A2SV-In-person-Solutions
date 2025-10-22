class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        cost_matrix = [[inf] * 26 for _ in range(26)]
        for a, b, c in zip(original, changed, cost):
            i = ord(a) - ord('a')
            j = ord(b) - ord('a')
            cost_matrix[i][j] = min(cost_matrix[i][j], c)
        
        for i in range(26):
            cost_matrix[i][i] = 0
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        ans = 0
        
        for i in range(len(source)):
            a, b = source[i], target[i]

            cost = cost_matrix[ord(a) - ord('a')][ord(b) - ord('a')]
            if cost == inf:
                return -1
            
            ans += cost

        return ans
        