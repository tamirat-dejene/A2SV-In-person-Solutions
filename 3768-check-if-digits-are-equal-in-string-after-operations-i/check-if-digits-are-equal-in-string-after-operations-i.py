class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            return s[0] == s[1]
        
        nxt = []
        for i in range(1, len(s)):
            nxt.append(str((int(s[i]) + int(s[i - 1])) % 10))
        
        return self.hasSameDigits(''.join(nxt))


        