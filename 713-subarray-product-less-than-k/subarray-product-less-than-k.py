class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        rprod, cnt, l = 1, 0, 0

        for r, num in enumerate(nums):
            rprod *= num

            while rprod >= k and l <= r:
                rprod /= nums[l]
                l += 1
            
            cnt += (r - l + 1)
        

        return cnt
        