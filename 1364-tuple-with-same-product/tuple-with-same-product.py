class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_matrix = [[a * b for a in nums] for b in nums]
        cnt = {}

        for i, row in enumerate(prod_matrix):
            for j, prod in enumerate(row):
                if i != j and i > j:
                    ans = cnt.get(prod, [])
                    ans.append([i, j])
                    cnt[prod] = ans
        
        sm = 0
        for k in cnt:
            indc =cnt[k]
            c = len(indc)


            sm += 4 * (c * (c - 1))

        return sm
        