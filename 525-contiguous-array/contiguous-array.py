class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        rsum, ans = 0, 0
        
        hmap = {0 : -1}

        for i, b in enumerate(nums):
            rsum += -1 if b == 0 else b

            if rsum in hmap:
                ans = max(ans, i - hmap[rsum])
            else:
                hmap[rsum] = i

        return ans

