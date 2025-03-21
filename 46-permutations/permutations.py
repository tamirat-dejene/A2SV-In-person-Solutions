class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, store):
            if len(nums) == 1: 
                res.append(store + nums)
                return res
            
            for i in range(len(nums)):
                store.append(nums[i])
                dfs(nums[:i] + nums[i + 1:], store)
                store.pop()
            
            return res
        
        return dfs(nums, [])