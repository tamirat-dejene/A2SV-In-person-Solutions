class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        l = 0 

        cnt = 0

        for r in range(len(nums)):

            if nums[r] != 0:
                l = r + 1

            cnt += (r - l + 1)
        
        return cnt
        