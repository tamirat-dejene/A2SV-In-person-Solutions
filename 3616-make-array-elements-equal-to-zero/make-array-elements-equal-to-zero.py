class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        psum = list(accumulate(nums))
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 0 and psum[-1] - psum[i] == (psum[i - 1] if i > 0 else 0):
                cnt += 2
            elif nums[i] == 0 and abs(psum[-1] - psum[i] - (psum[i - 1] if i > 0 else 0)) == 1:
                cnt += 1
        
        return cnt
        