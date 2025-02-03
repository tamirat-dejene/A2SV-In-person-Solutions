class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        for c in t:
            if not count.get(c, None) or count[c] <= 0: return False
            count[c] -= 1

        for v in count.values(): 
            if v != 0: return False
        return True

        