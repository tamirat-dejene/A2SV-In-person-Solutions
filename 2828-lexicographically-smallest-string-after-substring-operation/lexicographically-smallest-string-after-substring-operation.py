class Solution:
    def smallestString(self, s: str) -> str:
        s = [a for a in s]
        ai = [i for i in range(len(s)) if s[i] == 'a'] + [len(s)]

        l, done = 0, False

        for r in ai:
            for i in range(l, r):
                if s[i] != 'a':
                    done = True
                    s[i] = chr(ord(s[i]) - 1)

            if done: break
            l = r + 1
        
        if not done:
            s[-1] = 'z'

        return ''.join(s)
        
        


        


        
        