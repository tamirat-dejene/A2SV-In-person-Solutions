class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l, cnt = 0, 0
        mx, mn = 0, 0

        for r, num in enumerate(nums):
            if num > maxK or num < minK:
                l, mn, mx = r + 1, r + 1, r + 1
                continue

            if num == minK: mn = r
            if num == maxK: mx = r

            if nums[mn] == minK and nums[mx] == maxK:
                cnt += min(mx, mn) - l + 1
            
        return cnt
