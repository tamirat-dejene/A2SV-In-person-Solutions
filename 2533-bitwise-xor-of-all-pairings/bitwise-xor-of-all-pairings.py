class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) % 2 != len(nums2) % 2:
            if len(nums1) % 2 == 0:
                return reduce(xor, nums1)
            return reduce(xor, nums2)
        
        return 0 if len(nums1) % 2 == 0 else reduce(xor, nums1 + nums2)