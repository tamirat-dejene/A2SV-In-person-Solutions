class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dfs(num, nums, og):
            if not num:
                return og == 1 or (len(nums) > 1 and sum(nums) == og)
            
            for i in range(len(num)):
                nums.append(int(num[:i+1]))
                if dfs(num[i+1:], nums, og): return True
                nums.pop()
            
            return False

        return sum(k * k for k in range(1, n + 1) if dfs(str(k * k), [], k))
