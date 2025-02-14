class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count('0')

        ans, p, size = 0, 0, len(s)
        for i in range(zeros):
            while p < size:
                if s[p] == '0': break
                p += 1
            
            ans += p - i
            p += 1
        
        return ans

        