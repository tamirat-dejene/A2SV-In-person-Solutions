class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num, i = num[::-1], 0

        while i < len(num) and num[i] == '0':
            i += 1
        
        return num[i:][::-1]
        