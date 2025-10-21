class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def dfs(i, z=True):
            if (z and i >= N - 1) or i >= N:
                return 0

            return max(dfs(i + 1, z), nums[i] + dfs(i + 2, z))

        return max(nums[0] + dfs(2), dfs(1, False))