class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        s = 1
        right = True
        for i in range(1, time + 1):
            if s == n: right = False
            elif s == 1: right = True

            if right: s += 1
            else: s -= 1

        
        return s




            

        return s

        