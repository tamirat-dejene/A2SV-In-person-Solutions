class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            if set(word).issubset(set(allowed)): cnt += 1
        return cnt