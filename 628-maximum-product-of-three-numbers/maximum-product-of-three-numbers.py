class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        i, j, max_prod = 0, len(nums) - 1, float('-inf')

        while j - i >= 2:
            max_prod = max(
                max_prod,
                nums[i] * nums[i + 1] * nums[i + 2],
                nums[i] * nums[i + 1] * nums[j],
                nums[i] * nums[j - 1] * nums[j],
                nums[j - 2] * nums[j - 1] * nums[j]
            )
            i, j = i + 1, j - 1
        
        return max_prod


        




