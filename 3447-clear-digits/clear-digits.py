class Solution:
    def clearDigits(self, s: str) -> str:
        lst, charptr = list(s), -2

        for i, char in enumerate(lst):
            if char.isdigit():
                lst[i] = None
                if charptr == -2: charptr = i - 1 # init

                while charptr >= 0:
                    if lst[charptr] and lst[charptr].isalpha():
                        lst[charptr] = None
                        charptr -= 1
                        break
                    charptr -= 1
            else:
                charptr = i
        
        return ''.join([e for e in lst if e != None])