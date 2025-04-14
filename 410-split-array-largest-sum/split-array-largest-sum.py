class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(minimized):
            sm, cnt = 0, 1
            for num in nums:
                if sm + num > minimized:
                    sm = 0
                    cnt += 1
                sm += num
            
            return cnt <= k
        
        l, r = max(nums) - 1, sum(nums)

        while l + 1 < r:
            m = (l + r) // 2
            if check(m): r = m
            else: l = m

        return r


