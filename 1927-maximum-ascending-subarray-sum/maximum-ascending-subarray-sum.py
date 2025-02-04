class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        running_sum, max_sum, size = nums[0], nums[0], len(nums)

        for i in range(1, size):
            if nums[i] - nums[i - 1] > 0:
                running_sum += nums[i]
                if i == size - 1: max_sum = max(max_sum, running_sum)
            else:
                max_sum = max(running_sum, max_sum)
                running_sum = nums[i]
        return max_sum

        

        