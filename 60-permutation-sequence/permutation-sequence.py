class Solution:
    def getPermutation(self, n: int, k: int) -> str:


        def dfs(nums, lvl):
            nonlocal k
            if lvl == n:
                if k == 1: return ''.join(map(str, nums))
                k -= 1
                return ''
            
            for i in range(1, n + 1):
                if i not in nums: 
                    nums.append(i)
                    ans = dfs(nums, lvl + 1)
                    if ans: return ans
                    nums.pop()
        
        return dfs([], 0)
        