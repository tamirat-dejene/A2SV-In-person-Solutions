class NumArray:

    def __init__(self, nums: List[int]):
        ps = 0
        psum = []

        for num in nums:
            ps += num
            psum.append(ps)
        
        self.psum = psum

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.psum[right]
        return self.psum[right] - self.psum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)