class Solution:
    def maxFreqSum(self, s: str) -> int:
        count = Counter(s)
        
        v = max(count[c] for c in 'aeiou')
        c = max(count[c] for c in 'bcdfghjklmnpqrstvwxyz')

        return v + c
        