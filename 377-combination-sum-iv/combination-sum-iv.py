class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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
