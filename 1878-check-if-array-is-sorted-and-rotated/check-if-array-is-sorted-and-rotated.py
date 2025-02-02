class Solution:
    def check(self, nums: List[int]) -> bool:
        prev, nondec = -1, True

        for num in nums:
            if prev > 0:
                if num - prev < 0:
                    if nondec: nondec = False
                    else: return False
            prev = num
        
        return nondec or nums[-1] <= nums[0]


        