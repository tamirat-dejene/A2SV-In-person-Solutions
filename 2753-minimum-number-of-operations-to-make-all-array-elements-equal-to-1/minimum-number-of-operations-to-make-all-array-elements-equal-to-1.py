class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) != 1:
            return -1
        ans, N = inf, len(nums)


        if 1 in nums:
            return N - nums.count(1)

        for s in range(1, N):
            c, g = 0, nums[s - 1]

            for i in range(s, N):
                g = gcd(g, nums[i])
                c += 1
                if g == 1:
                    break
            
            if g == 1:
                ans = min(ans, c + N - 1)

        return ans
        