class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k, stack = float('-inf'), []
        i = len(nums) - 1
        
        while i >= 0:
            curr = nums[i]
            if curr < k: return True

            while stack and stack[-1] < curr:
                k = stack.pop()
            
            stack.append(curr)
            i -= 1
        
        return False



