class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l + 1 < r:

            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m
        
        return min(nums[l], nums[r])

        