class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        st = set(cnt.values())
        return len(st) <= 1
        

        