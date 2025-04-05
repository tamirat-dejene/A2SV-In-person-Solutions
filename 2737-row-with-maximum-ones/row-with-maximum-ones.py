class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return max([[i, sum(row)] for i, row in enumerate(mat)], key=lambda itm : itm[1])