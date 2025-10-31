class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        x = 0
        N = len(nums)

        for i in range(2**N):
            xx, k = 0, 0

            while k < N:
                if i & 1:
                    xx ^= nums[k]
                
                k += 1
                i >>= 1

            x += xx
        
        return x




        