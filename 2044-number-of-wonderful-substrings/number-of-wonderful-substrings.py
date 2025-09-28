class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        xor = 0
        res = 0
        freq = {0:1}

        for c in word:
            bit = ord(c) - ord('a')
            xor ^= (1 << bit)

            if xor in freq:
                res += freq[xor]
                freq[xor] += 1
            else:
                freq[xor] = 1

            for odd_c in range(10):
                if xor ^ (1 << odd_c) in freq:
                    res += freq[xor ^ (1 << odd_c)]

        return res
