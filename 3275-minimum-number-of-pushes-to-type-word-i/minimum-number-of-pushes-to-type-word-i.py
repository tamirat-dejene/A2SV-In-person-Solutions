class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        q, r = n // 8, n % 8
        c = r * (q + 1)

        for m in range(1, q + 1):
            c += (m * 8)
        
        return c
    