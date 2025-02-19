class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0

        ones = s.count('1')
        zeros = 0
        l = 0

        while l < len(s) - 1:
            if s[l] == '0': zeros += 1
            else: ones -= 1

            ans = max(ans, zeros + ones)
            l += 1
        
        return ans

        