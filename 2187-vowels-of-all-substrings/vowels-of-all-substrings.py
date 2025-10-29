class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)

        return sum((i + 1) * (N - i) for i in range(N) if word[i] in 'aeiou')
        