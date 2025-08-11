class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        ln = len(nums)
        srted = sorted(nums)
        shift = (ln - nums.index(srted[0])) % ln

        for i in range(ln):
            if srted[(i + shift) % ln] != nums[i]:
                return -1
        
        return shift
        

        