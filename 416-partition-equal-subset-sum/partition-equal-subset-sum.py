class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        tot = sum(nums)
        if tot % 2 != 0: return False
        h = tot // 2
        dp = [True] + [False] * h

        dp2 = [True] + [False] * h
        for i in range(N - 1, -1, -1):
            for sm in range(nums[i], h + 1):
                dp2[sm] = dp[sm - nums[i]] or dp[sm]
            dp = dp2[:]
            
        return dp[h]

        def dfs(i, sm):
            if i == N or sm == 0:
                return sm == 0

            if dfs(i + 1, sm - nums[i]) or dfs(i + 1, sm):
                return True

            return False

        return dfs(0, tot // 2)