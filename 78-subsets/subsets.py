class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # ss = []

        # def dfs(i=0):
        #     if i >= len(nums):
        #         ans.append(ss[:])
        #         return
            
        #     ss.append(nums[i])
        #     dfs(i + 1)
        #     ss.pop()
        #     dfs(i + 1)
        
        # dfs()

        # return ans

        n = len(nums)
        ans = []

        for i in range(2**n):
            k = 0
            keep = []

            while i > 0:
                if i & 1:
                    keep.append(nums[k])
                i >>= 1
                k += 1
            
            ans.append(keep)
        return ans


            
                

        