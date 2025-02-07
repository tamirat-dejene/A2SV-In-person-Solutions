class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        idx_sm = {}

        for i, row in enumerate(nums):
            for j, cell in enumerate(row):
                v = idx_sm.get(i + j, [])
                v.append(cell)
                idx_sm[i + j] = v

        res = []
        for sm in sorted(idx_sm):
            for v in idx_sm[sm][::-1]: res.append(v)
        
        return res