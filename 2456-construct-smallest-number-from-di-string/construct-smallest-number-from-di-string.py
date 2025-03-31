class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # stack = []
        # ans = []
        # for i, p in enumerate(pattern):

        #     if p == 'D':
        #         stack.append(i + 1)
        #     else:
        #         ans.append(i + 1)

        #     while stack and p == 'I':
        #         ans.append(stack.pop())
            
        # ans.append(len(pattern) + 1)
        # while stack: ans.append(stack.pop())

        # return ''.join(str(n) for n in ans)

        ln = len(pattern)

        def match(nums):
            for i in range(ln):
                if pattern[i] == 'D' and nums[i + 1] > nums[i]: return False
                if pattern[i] == 'I' and nums[i + 1] < nums[i]: return False
            
            return ''.join(map(str, nums))

        def dfs(c=0, nums=[]):
            nonlocal ln
            
            if c == ln + 1: return match(nums)
            
            for n in range(1, 10):
                if n in nums: continue
                nums.append(n)
                res = dfs(c + 1, nums)
                if res: return res
                nums.pop()

        return dfs()
                
        



                