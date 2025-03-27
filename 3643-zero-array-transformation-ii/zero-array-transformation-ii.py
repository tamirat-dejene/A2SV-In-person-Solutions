class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        size = len(nums) + 1

        def check_prefix(ln):
            nonlocal size
            pref = [0] * (size + 1)

            for i in range(ln):
                l, r, v = queries[i]
                pref[l] += v
                pref[r + 1] -= v
            
            for i in range(1, size + 1):
                pref[i] += pref[i - 1]
            
            for v, a in zip(pref, nums): 
                if v < a: return False
            
            return True
        
        if not check_prefix(len(queries)): return -1
        
        l, r = -1, len(queries)

        while l + 1 < r:
            m = (l + r) // 2

            if check_prefix(m): r = m
            else: l = m
        
        return r