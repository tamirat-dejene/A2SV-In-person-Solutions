class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        nums = [int(num) for num in s.split() if is_integer(num)]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= 0: return False
        return True