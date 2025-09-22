class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0: return False
        
        @cache
        def dp(sm, j):
            if sm <= 0:
                return sm == 0

            for i in range(j, len(nums)):
                if dp(sm - nums[j], i + 1):
                    return True
            
            return False
                
        return dp(tot // 2, 0)



        

        
