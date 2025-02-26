class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        largest_pos, smallest_neg = 0, 0

        psum = 0

        ans = float('-inf')
        
        for num in nums:
            psum += num

            if psum >= 0:
                ans = max(ans, abs(psum - smallest_neg))
                largest_pos = max(largest_pos, psum)
            else:
                ans = max(ans, abs(psum - largest_pos))
                smallest_neg = min(smallest_neg, psum)
        
        return ans