class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        for i in range(p, len(nums)):
            if nums[i] == 1:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        return nums
        