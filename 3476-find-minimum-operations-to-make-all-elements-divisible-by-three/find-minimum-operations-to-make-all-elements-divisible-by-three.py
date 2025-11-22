class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(num - (num // 3) * 3, 3 * ceil(num / 3) - num) for num in nums)
        