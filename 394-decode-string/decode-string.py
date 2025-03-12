class Solution:
    def decodeString(self, s: str) -> str:
        string = list(s)

        '''
            - Iterate over the string characters
            -    3[a2[c]]3[a]2[bc]   
            -    3*f(a + 2*f(c)) + 3*f(a) + 2*f(bc)
        '''

        def decoder(start, end):
            nonlocal string

            digits, alphas = [], [] # chars and digts before the outermost brket(if there is any)
            brkt_cnt, br_st = 0, -1 # to get the outermost bracket for recursion
            
            for p in range(start, end + 1):
                char = string[p]

                if char.isalpha() and brkt_cnt == 0: alphas.append(char)
                elif char.isdigit() and brkt_cnt == 0: digits.append(char)
                elif char == '[':
                    if br_st == -1: br_st = p
                    brkt_cnt += 1
                elif char == ']':
                    brkt_cnt -= 1

                    # balanced
                    if brkt_cnt == 0: 
                        return ''.join(alphas) + decoder(br_st + 1, p - 1) * int(''.join(digits)) + decoder(p + 1, end)
               
            # basecase 
            return ''.join(alphas)
        
        ans = decoder(0, len(string) - 1)
        return ans