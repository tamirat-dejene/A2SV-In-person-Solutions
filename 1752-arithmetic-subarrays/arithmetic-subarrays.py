class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        for l, r in zip(l, r):
            curr, p = sorted(nums[l:r+1]), True

            for i in range(1, r - l):
                if 2 * curr[i] != curr[i + 1] + curr[i - 1]:
                    p = False
                    break

            ans.append(p)

        return ans
        