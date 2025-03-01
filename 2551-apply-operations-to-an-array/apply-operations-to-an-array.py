class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = [num for num in nums if num != 0]
        return res + [0] * (size - len(res))
        
        