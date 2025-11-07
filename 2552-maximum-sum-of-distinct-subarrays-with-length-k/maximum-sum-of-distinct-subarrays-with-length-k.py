class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l, N = 0, len(nums)
        store, ans, sm = {}, 0, 0
        
        for r in range(N):
            if nums[r] in store:
                while nums[r] in store:
                    sm -= nums[l]
                    store.pop(nums[l])
                    l += 1
            
            store[nums[r]] = r
            sm += nums[r]

            if r - l + 1 == k:
                store.pop(nums[l])
                ans = max(sm, ans)
                sm -= nums[l]
                l += 1

        return ans



        