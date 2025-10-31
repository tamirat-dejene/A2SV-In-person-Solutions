class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        store = {0:-1}
        
        ans = len(nums)
        rsum = 0

        for i, num in enumerate(nums):
            rsum += num
            store[rsum % p] = i

            if (rsum - tot) % p in store:
                ans = min(ans, i - store[(rsum - tot) % p])
            

        return -1 if ans == len(nums) else ans
        