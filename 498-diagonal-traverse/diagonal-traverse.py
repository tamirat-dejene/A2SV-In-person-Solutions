class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j, nex, ney, swx, swy, ne = 0, 0, -1, 1, 1, -1, True
        m, n, res = len(mat), len(mat[0]), []

        def in_bound(i, j): return [0 <= i < m,  0 <= j < n]

        def valid_next_move(i, j, ne):
            i, j = i + (nex if ne else swx), j + (ney if ne else swy)
            i_in_bound, j_in_bound = in_bound(i, j)
            
            if ne: 
                if (i_in_bound and not j_in_bound) or (not i_in_bound and not j_in_bound):
                    i += 2
                    j -= 1
                elif not i_in_bound and j_in_bound:
                    i += 1
                else: return [i, j, ne]
            else:
                if (not i_in_bound and j_in_bound) or (not i_in_bound and not j_in_bound):
                    j += 2
                    i -= 1
                elif i_in_bound and not j_in_bound:
                    j += 1
                else: return [i, j, ne]
            
            return [i, j, not ne]
                


        for _ in range(n * m):
            res.append(mat[i][j])
            i, j, ne = valid_next_move(i, j, ne)
        
        return res