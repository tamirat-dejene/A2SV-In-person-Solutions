class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        s = len(nums) 

        return s * (s + 1) // 2 - sum(nums)