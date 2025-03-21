class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def dfs(p=0, store=[]):
            if len(store) >= 3:
                if (store[-1] != store[-2] + store[-3]): return False
                elif p >= len(num): return True

            for i in range(p, len(num)):
                if num[p:i+1] != str(int(num[p:i+1])): return False # leading zero

                store.append(int(num[p:i+1]))
                if dfs(i+1, store): return True
                store.pop()

            return False

        return dfs()