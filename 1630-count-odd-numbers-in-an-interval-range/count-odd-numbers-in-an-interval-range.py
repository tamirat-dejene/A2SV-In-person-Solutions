class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a1 = low if low % 2 == 1 else low + 1
        an = high if high % 2 == 1 else high - 1

        if an < a1:
            return  0

        return (an - a1) // 2 + 1
        