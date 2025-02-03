class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag = False
        i = left
        while i <= right:
            for x, y in ranges:
                if x <= i <= y:
                    flag = True
                    break     
            
            if not flag: return flag
            i, flag = i + 1, False 

        return True