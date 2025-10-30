class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        store = Counter(nums)

        for num in list(set(nums)):
            cn = store[num]
            cc = store[k - num]

            if num != k - num:
                rm = min(cn, cc)
            else:
                rm = cn // 2

            ans += rm
            
            store[num] -= max(rm, store[num])
            store[k - num] -= max(rm, store[k - num])
        
        return ans
        