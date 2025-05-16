class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lft, rgt = left, right
        
        bl = bin(left)[2:]
        br = bin(right)[2:]

        if len(bl) == len(br):
            k = len(bl)

            while lft or rgt:
                if lft == rgt:
                    break
                lft >>= 1
                rgt >>= 1
                
            return rgt << (k - len(bin(rgt)[2:]))

        else:
            return 0