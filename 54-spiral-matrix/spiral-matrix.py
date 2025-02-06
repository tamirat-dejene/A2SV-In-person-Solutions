class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []

        while t <= b and l <= r:
            # top row
            for col in range(l, r + 1): res.append(matrix[t][col])
            t += 1
            # right col
            for row in range(t, b + 1): res.append(matrix[row][r])
            r -= 1
            # bottom row
            if  b != t - 1:
                for col in range(r, l - 1, -1): res.append(matrix[b][col])
            b -= 1
            # left col
            if r != l - 1:
                for row in range(b, t - 1, -1): res.append(matrix[row][l])
            l += 1


        return res
        