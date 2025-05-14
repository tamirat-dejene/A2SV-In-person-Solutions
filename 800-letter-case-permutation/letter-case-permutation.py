class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        ans = set()

        for i in range(2**len(s)):
            k = 0
            lw, up = [], []

            while k < len(s):
                if (i & 1) and (s[k].isalpha()):
                    lw.append(s[k].lower())
                    up.append(s[k].upper())
                else:
                    lw.append(s[k])
                    up.append(s[k])
            
                i >>= 1
                k += 1
            
            ans.add(''.join(lw))
            ans.add(''.join(up))

        return list(ans)
            


