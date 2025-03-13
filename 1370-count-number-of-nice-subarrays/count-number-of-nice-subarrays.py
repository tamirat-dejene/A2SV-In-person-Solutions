class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, cnt_odd, res = 0, 0, 0

        for r, num in enumerate(nums):
            if num % 2 == 1: cnt_odd += 1

            while cnt_odd > k:
                if nums[l] % 2 == 1: cnt_odd -= 1
                l += 1

            if cnt_odd == k:
                near_left = l
                while near_left <= r and nums[near_left] % 2 == 0:
                    near_left += 1
                res += (near_left - l + 1)

        return res

        