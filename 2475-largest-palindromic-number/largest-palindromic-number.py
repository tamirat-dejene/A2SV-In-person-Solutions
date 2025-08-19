class Solution:
    def largestPalindromic(self, num: str) -> str:
        ans = []
        cnt = Counter(num)

        for i in '9876543210':
            if i == '0' and not ans:
                break
            
            c = i * ((cnt[i] - (0 if cnt[i] % 2 == 0 else 1)) // 2)
            
            if c: ans.append(c)
            
            cnt[i] = 0 if cnt[i] % 2 == 0 else 1
    
        ans = ''.join(ans)
        
        for i in '9876543210':
            if i == '0' and not ans:
                return '0'
            if cnt[i] == 1:
                return ans + i + ans[::-1]
        
        return ans + ans[::-1] 

        