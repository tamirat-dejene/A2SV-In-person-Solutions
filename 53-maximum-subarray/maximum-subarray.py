class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx, rsum = float('-inf'), 0

        for num in nums:
            rsum += num
            mx = max(mx, rsum)

            if rsum < 0: rsum = 0
        
        return mx