class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sl = []
        cnt = defaultdict(int)
        md = 10**9 + 7
        res = 0 

        for i, num in enumerate(instructions):
            r = bisect_right(sl, num)
            res += min(r - cnt[num], i - r)
            res %= md

            sl[r:r] = [num] # If this is AC, python's slice is crazy fast than SortedList :D
            cnt[num] += 1
        
        return res 