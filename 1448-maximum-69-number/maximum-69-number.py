class Solution:
    def maximum69Number (self, num: int) -> int:
        string = list(str(num))

        if '6' not in string:
            return num
        
        string[string.index('6')] = '9'
        
        return int(''.join(string))
        