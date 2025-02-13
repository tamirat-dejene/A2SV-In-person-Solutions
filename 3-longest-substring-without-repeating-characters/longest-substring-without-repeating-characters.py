class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, ans, size, l = {}, 0, len(s), 0
       
        for i, c in enumerate(s):
            if c in seen and seen[c] >= l: 
                ans = max(ans, i - l)
                l = seen[c] + 1 
            
            if i + 1 >= size: ans = max(ans, i - l + 1) # last iteration

            seen[c] = i
        return ans
        
        
        