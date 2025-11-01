class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = lambda num: int(str(num)[::-1])
        cnt, ans = defaultdict(int), 0

        for num in nums:
            rv = rev(num)
            ans += cnt[num - rv]
            cnt[num - rv] += 1
        
        return ans % (10**9 + 7)
        