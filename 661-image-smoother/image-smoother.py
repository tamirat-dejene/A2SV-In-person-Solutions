class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                sm, cnt = img[i][j], 1

                if i - 1 >= 0: sm, cnt = sm + img[i-1][j], cnt + 1
                if i + 1 < m: sm, cnt = sm + img[i+1][j], cnt + 1
                if j - 1 >= 0: sm, cnt = sm + img[i][j-1], cnt + 1
                if j + 1 < n: sm, cnt = sm + img[i][j+1], cnt + 1

                if i - 1 >= 0 and j - 1 >= 0: sm, cnt = sm + img[i-1][j-1], cnt + 1
                if i - 1 >= 0 and j + 1 < n: sm, cnt = sm + img[i-1][j+1], cnt + 1
                if i + 1 < m and j - 1 >= 0: sm, cnt = sm + img[i+1][j-1], cnt + 1
                if i + 1 < m and j + 1 < n: sm, cnt = sm + img[i+1][j+1], cnt + 1

                res[i][j] = sm // cnt
        
        return res
            


        