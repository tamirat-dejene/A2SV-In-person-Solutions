class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        r = 0

        while r < N:
            if nums[r] == 1:
                l, r = r + 1, r + 1

                while r < N and nums[r] != 1:
                    r += 1
                    
                if r < N and r - l < k:
                    return False
            else:
                r += 1

        return True
            


        
