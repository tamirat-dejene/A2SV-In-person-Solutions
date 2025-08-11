class Solution:
    def reconstructMatrix(self, u: int, l: int, colsum: List[int]) -> List[List[int]]:
        c = len(colsum)
        res = [[0]*c for _ in range(2)]
        one = 0

        for i in range(c):
            if colsum[i] == 0: 
                continue
            elif colsum[i] == 1:
                one += 1
            else:
                res[0][i], res[1][i] = 1, 1
        
        up = u - sum(res[0])
        lo = l - sum(res[1])

        if up + lo != one:
            return []
        
        for i in range(c):
            if one == 0: break
            if colsum[i] == 1:
                if up != 0:
                    res[0][i] = 1
                    up -= 1
                elif lo != 0:
                    res[1][i] = 1
                    lo -= 1
                one -= 1
        return res if sum(res[0]) == u and sum(res[1]) == l else []