class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l + 2 < r:
            m = (l + r) // 2

            if arr[m - 1] > arr[m] > arr[m + 1]: r = m
            else: l = m
        
        mx = max(arr[l], arr[l + 1], arr[r])
        
        return l if mx == arr[l] else l + 1 if mx == arr[l + 1] else r
        