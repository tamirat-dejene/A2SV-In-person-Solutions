class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(list) #[count, index]
        l, cnt = 0, 0
        
        for r, num in enumerate(nums):
            if num in hmap:
                hmap[num][0] += 1
                hmap[num][1] = r
            else:
                hmap[num] = [1, r]

            while len(hmap) > k and l <= r:
                hmap[nums[l]][0] -= 1
                if hmap[nums[l]][0] == 0: 
                    hmap.pop(nums[l])
                l += 1
            
            if len(hmap) == k: 
                min_idx = min(itm[1] for itm in hmap.values())
                cnt += min_idx - l + 1
        
        return cnt

        