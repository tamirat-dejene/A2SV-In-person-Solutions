class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        cd = [a - b for a, b in zip(nums1, nums2)]
        # srtd = SortedList(cd)
        # ln = len(srtd)
        # ans = 0
        # for d in cd:
        #     srtd.remove(d)
        #     ln -= 1
        #     ans += ln - bisect_left(srtd, d - diff)
        
        srtd = []
        ln = 0
        ans = 0

        for i in range(len(cd) - 1, -1, -1):
            l = bisect_left(srtd, cd[i] - diff)
            ans += ln - l

            p = bisect_left(srtd, cd[i])
            srtd[p:p] = [cd[i]]
            ln += 1

        return ans