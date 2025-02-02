class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(); ans, prev = 1, 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == prev: continue
            prev = nums[i] # optmization

            j, temp = i - 1, k
            
            while j >= 0  and temp > 0:
                temp -= (nums[i] - nums[j])
                if temp >= 0: j -= 1

            ans = max(ans, i - j)
        
        return ans