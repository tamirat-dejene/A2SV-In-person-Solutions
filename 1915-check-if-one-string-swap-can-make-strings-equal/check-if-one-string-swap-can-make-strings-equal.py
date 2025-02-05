class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap1, swap2, ready, swapped = '', '', False, False
        for i, [c1, c2] in enumerate(zip(s1, s2)):
            if c1 != c2:
                if swapped: return False
                if not ready:
                    swap1, swap2, ready = c1, c2, True
                else:
                    if swapped or not (c1 == swap2 and c2 == swap1): return False
                    ready, swapped = False, True
        
        return not ready or swapped


        