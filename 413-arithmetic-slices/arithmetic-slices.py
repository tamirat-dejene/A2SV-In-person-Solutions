class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        print(diff)

        if not diff:
            return 0

        p = diff[0]
        cnt = 1
        ans = 0
        for i in range(1, len(diff)):
            if diff[i] == p:
                cnt += 1
            else:
                cnt = 1
            
            ans += (cnt - 1)

            p = diff[i]
        
        return ans
            
                  





        return 0

        