class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        store = [dict() for _ in range(N)]

        def dfs(i, sm=0):
            if i == N:
                return 1 if sm == target else 0
            
            if sm not in store[i]:
                store[i][sm] = dfs(i + 1, sm + nums[i]) + dfs(i + 1, sm - nums[i])
            
            return store[i][sm]
            
        return dfs(0)