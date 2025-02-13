class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        if nums[0] >= k: return 0
        cnt = 0
        while len(nums) >= 2:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            cnt += 1
            if nums[0] >= k: return cnt
        