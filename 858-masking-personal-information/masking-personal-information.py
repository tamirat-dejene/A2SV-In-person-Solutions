class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s=s.lower()
            name = s[:s.index('@')]
            name = name[0] + '*'*5 + name[-1]

            return ''.join([name, s[s.index('@'):]])
        
        digits = [n for n in s if n.isalnum()]
        print(digits)
        return '-'.join([
            ('' if len(digits) == 10 else '+') + '*'*(len(digits) % 10),
            '*'*3,
            '*'*3,
            ''.join(digits[-4:])
            ])[1 if len(digits) == 10 else 0:]
        
        

        