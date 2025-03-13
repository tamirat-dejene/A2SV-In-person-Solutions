class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        l, ans, cnt_mx = 0, 0, 0

        for r, num in enumerate(nums):
            if num == mx: cnt_mx += 1

            while l <= r and (nums[l] != mx or cnt_mx > k): 
                if nums[l] == mx: cnt_mx -= 1
                l += 1

            if cnt_mx >= k: ans += l + 1
        
        return ans


        