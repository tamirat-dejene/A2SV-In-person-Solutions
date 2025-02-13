class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        ans = nums[0] + nums[1] + nums[-1]

        for k in range(size - 2):
            l, r = k + 1, size - 1

            while l < r:
                sm = nums[l] + nums[r] + nums[k]
                
                ans = sm if abs(target - sm) <= abs(target - ans) else ans

                if sm < target: l += 1
                elif sm > target: r -= 1
                else: return target

        return ans