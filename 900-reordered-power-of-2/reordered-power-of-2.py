class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        lst = list(str(n))

        for p in permutations(lst):
            if p[0] == '0':
                continue
            num = int(''.join(a for a in p))

            if num & (num - 1) == 0: 
                return True
        
        return False



        # def dfs(coll):
        #     if len(coll) == len(lst):
        #         num = int(''.join(lst[j] for j in coll))

        #         if num & (num - 1) == 0:
        #             return True

        #     for i in range(len(lst)):
        #         if i in coll or (len(coll) >= 1 and lst[coll[0]] == '0'): 
        #             continue
        #         coll.append(i)

        #         if dfs(coll): 
        #             return True

        #         coll.pop()

        #     return False       
        # return dfs([])