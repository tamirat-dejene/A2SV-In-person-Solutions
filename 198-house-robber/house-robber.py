class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}

        def dp(n):
            if n >= len(nums):
                return 0

            if n not in store:
                store[n] = nums[n] + max(dp(n + 2), dp(n + 3))

            return store[n]

        return max(dp(0), dp(1))