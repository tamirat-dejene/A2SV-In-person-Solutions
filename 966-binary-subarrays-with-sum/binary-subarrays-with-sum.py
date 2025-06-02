class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hmap = {0:1}

        rsum = 0

        ans = 0
        for num in nums:
            rsum += num
            if rsum - goal in hmap:
                ans += hmap[rsum - goal]
            
            hmap[rsum] = hmap.get(rsum, 0) + 1
        
        return ans