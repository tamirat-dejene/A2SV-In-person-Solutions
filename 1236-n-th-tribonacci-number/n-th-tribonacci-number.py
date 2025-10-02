class Solution:
    def tribonacci(self, n: int) -> int:
        trie = [0, 1, 1]

        for i in range(3, n + 1):
            trie = [trie[-2], trie[-1], trie[-1] + trie[-2] + trie[-3]]

        return trie[-1 if n >= 3 else n]

        