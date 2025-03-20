class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ss = []

        def dfs(i=0):
            if i >= len(nums):
                ans.append(ss[:])
                return
            
            ss.append(nums[i])
            dfs(i + 1)
            ss.pop()
            dfs(i + 1)
            
        
        dfs()

        return ans
        