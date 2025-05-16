class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda p, c: c ^ p, nums, 0)