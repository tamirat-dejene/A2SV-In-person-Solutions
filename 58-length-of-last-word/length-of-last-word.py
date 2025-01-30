class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt, cnted = 0, False
        for char in s[::-1]:
            if char != ' ':
                cnted =True
                cnt += 1
            elif cnted: return cnt
        return cnt

        