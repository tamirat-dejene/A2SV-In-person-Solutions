class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        size, ans, prefix = len(nums), 0, nums[::]

        for i in range(2, size):
            prefix[i] += prefix[i - 2]
        prefix = [0, 0] + prefix
        
        ev_sm, od_sm = prefix[-2], prefix[-1]

        if size % 2 == 1: 
            ev_sm, od_sm = od_sm, ev_sm


        ans = 0
        
        for i, num in enumerate(nums):
            od_pref = prefix[i + 1]
            ev_pref = prefix[i]

            od_suff = od_sm - od_pref
            ev_suff = ev_sm - prefix[i + 2]
            
            if i % 2 == 1:
                od_pref, ev_pref = ev_pref, od_pref
                od_suff = od_sm - prefix[i + 2]
                ev_suff = ev_sm - ev_pref

            if od_pref + ev_suff == ev_pref + od_suff:
                ans += 1
        
        return ans
                
        
        
        





        