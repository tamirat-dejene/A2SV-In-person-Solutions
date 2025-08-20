class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i == n - 1:
                return nums[i]

            if i == n - 2:
                return max(nums[i], nums[i + 1])

            if i not in memo:
                memo[i] = max(dp(i + 1), dp(i + 2) + nums[i])
            
            return memo[i]
        
        return dp(0)

        