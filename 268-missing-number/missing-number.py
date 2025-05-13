class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # s = len(nums) 

        # return s * (s + 1) // 2 - sum(nums)
        tot_ = 0
        val_ = 0

        for i, num in enumerate(nums):
            tot_ ^= (i + 1)
            val_ ^= num
        
        return tot_ ^ val_