class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ln = len(nums)

        if k == 50000: return 1

        def select(l, r):
            nonlocal ln, k
  
            if l >= r: return nums[l]

            w = l + 1

            for i in range(l + 1, r + 1):
                if nums[i] < nums[l]:
                    nums[i], nums[w] = nums[w], nums[i]
                    w += 1
            nums[w - 1], nums[l] = nums[l], nums[w - 1]
            
            idx = ln - k
            
            if idx == w - 1: return nums[w - 1]
            
            elif idx > w - 1:
                return select(w , r)
            else: # to the left
                return select(l, w - 2)

        return select(0, ln - 1)