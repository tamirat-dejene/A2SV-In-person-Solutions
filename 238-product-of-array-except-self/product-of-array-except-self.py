class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp, sp = [], []
        size, p, s = len(nums), 1, 1
        
        for i in range(size):
            p *= nums[i]
            s *= nums[size - i - 1]

            pp.append(p)
            sp.append(s)
        
        sp = sp[::-1]
        
        print(pp, sp)
        
        nums[0], nums[size - 1] = sp[1], pp[size - 2]

        for i in range(1, size - 1):
            nums[i] = pp[i - 1] * sp[i + 1]
        
        return nums
        
        