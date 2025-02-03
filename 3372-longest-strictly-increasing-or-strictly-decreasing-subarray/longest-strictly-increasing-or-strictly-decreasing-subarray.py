class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i, j, max_strict, size = 1, 0, 1, len(nums)
        dir_ = 0 if len(nums) <= 1 else 1 if nums[1] - nums[0] >= 0 else -1

        while i < size:
            diff = nums[i] - nums[i - 1]
            if diff == 0:
                max_strict = max(max_strict, i - j)
                j, dir_ = i, 1
            elif (diff > 0 and dir_ != 1) or (diff < 0 and dir_ != -1):
                max_strict = max(max_strict, i - j)
                j, dir_ = i - 1, 1 if diff > 0 else -1
            
            i += 1
            if i == size: max_strict = max(max_strict, i - j) # the last iteration
        
        return max_strict