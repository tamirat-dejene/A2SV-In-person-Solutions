class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ln = len(nums)
        pref = 0
        ans = 0
        l = 0

        for r in range(ln):
            while nums[r] & pref != 0:
                pref ^= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
            
            pref |= nums[r]
        
        return ans