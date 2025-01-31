class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(s) for n in nums for s in str(n)]

        