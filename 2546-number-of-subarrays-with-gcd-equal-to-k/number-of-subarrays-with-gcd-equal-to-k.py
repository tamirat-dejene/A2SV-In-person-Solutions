class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        N, ans = len(nums), 0
        for i in range(N):
            if nums[i] % k != 0: continue
            gc = nums[i]
            for j in range(i, N):
                if nums[j] % k != 0:
                    break
                gc = gcd(gc, nums[j])
                if gc == k: ans += 1
        return ans
        