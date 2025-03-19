class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []

        def solve(store=[]):
            nonlocal n, k

            if len(store) == k:
                ans.append(store)
                return
            
            for i in range(1 if not store else store[-1] + 1, n + 1):
                store.append(i)
                solve(store[:])
                store.pop()

        solve()

        return ans
        