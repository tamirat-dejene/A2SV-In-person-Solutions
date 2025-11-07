class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N, l, inv = len(nums), 0, 0
        
        ans = []

        for r in range(N):
            if r > 0 and nums[r] != nums[r - 1] + 1:
                inv = r - l

            if r - l + 1 == k:
                if inv == 0:
                    ans.append(nums[r])
                else:
                    ans.append(-1)
                    inv -= 1
                
                l += 1
            
        return ans