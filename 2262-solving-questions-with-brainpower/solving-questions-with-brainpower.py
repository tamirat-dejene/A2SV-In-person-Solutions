class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        store = [-1] * N

        def dfs(idx):
            if idx >= N:
                return 0
            
            if store[idx] == -1:
                store[idx] = max(questions[idx][0] + dfs(idx + questions[idx][1] + 1), dfs(idx + 1))
            
            return store[idx]
        
        return dfs(0)
        