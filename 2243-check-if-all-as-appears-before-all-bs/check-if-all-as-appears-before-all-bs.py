class Solution:
    def checkString(self, s: str) -> bool:
        seen_a, seen_b = False, False

        for char in s:
            if char == 'a':
                if seen_b: return False
                seen_a = True
            else:
                seen_b = True
        return True


        