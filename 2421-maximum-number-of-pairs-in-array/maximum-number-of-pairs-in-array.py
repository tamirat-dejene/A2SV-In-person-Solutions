class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt= Counter(nums)
        p, l = 0, 0
        for n in cnt:
            if cnt[n] % 2 == 0: p += cnt[n] // 2
            else:
                p += (cnt[n] // 2)
                l += cnt[n] % 2
        
        return [p, l]
