class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, size = 0, len(nums)
        jumps = nums[0]

        for i, num in enumerate(nums):
            if i == size - 1: return True
            if jumps == 0 and num == 0: return False

            jumps = max(num, jumps) - 1

        return False
        