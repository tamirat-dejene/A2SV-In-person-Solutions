class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # digit_sum: [a, b]
        store, res = defaultdict(list), -1
        for num in nums:
            d_sum = sum(map(int, list(str(num))))
            if d_sum in store:
                pairs = sorted([*store.get(d_sum), num])
                store[d_sum] = pairs if len(pairs) ==  2 else [pairs[1], pairs[2]]
                res = max(res, sum(store[d_sum]))
            else:
                store[d_sum] = [num]            
        
        return res