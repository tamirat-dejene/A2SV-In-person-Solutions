class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        N, ans = len(nums), 0
        for i in range(N):
            gc = nums[i]
            for j in range(i, N):
                gc = gcd(gc, nums[j])
                if gc == k: ans += 1
        return ans
        