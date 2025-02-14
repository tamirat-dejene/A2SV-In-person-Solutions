class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lst, l, m, r):
            a, b, res = l, m + 1, []

            while a <= m and b <= r:
                if lst[a] <= lst[b]:
                    res.append(lst[a]); a += 1
                else:
                    res.append(lst[b]); b += 1
            while a <= m:
                res.append(lst[a]); a+= 1
            while b <= r:
                res.append(lst[b]); b+= 1
            

            for s in res:
                lst[l] = s
                l += 1
            

        
        def merge_sort(lst, l, r):
            if l >= r: return
            mid = (l + r) // 2
            merge_sort(lst, l, mid)
            merge_sort(lst, mid + 1, r)
            merge(lst, l, mid, r)
        
        merge_sort(nums, 0, len(nums) - 1)
        return nums




            
            

        