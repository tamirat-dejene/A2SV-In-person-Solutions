class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        N, i, j = len(nums), {}, {}

        ans = -1

        for k, num in enumerate(nums):
            if num in j:
                d1 = j[num] - i[num]
                d2 = k - j[num]
                d3 = d1 + d2

                if ans == -1:
                    ans = d1 + d2 + d3
                
                ans = min(ans, d1 + d2 + d3)
                i[num] = j[num]
                j[num] = k

            elif num in i:
                j[num] = k
            else:
                i[nums[k]] = k
        
        return ans
        