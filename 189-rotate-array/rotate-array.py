class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        keep, size = nums.copy(), len(nums)

        for i in range(size): 
            nums[i] = keep[(size - k + i) % size]