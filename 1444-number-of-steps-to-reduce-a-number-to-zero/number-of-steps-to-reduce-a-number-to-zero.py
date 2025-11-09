class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return (1 if num % 2 == 0 or num == 1 else 2) + self.numberOfSteps(num // 2)