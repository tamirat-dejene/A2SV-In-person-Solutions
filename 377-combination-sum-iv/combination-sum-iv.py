class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        nums.sort()

        for rem in range(target + 1):
            for num in nums:
                if num <= rem:
                    dp[rem] += dp[rem - num]
                else:
                    break
        
        return dp[target]

        @cache
        def dfs(sm):
            if sm == 0:
                return 1
            if sm < 0:
                return 0
            tot = 0
            for num in nums:
                tot += dfs(sm - num)
            
            return tot
            
        return dfs(target)
