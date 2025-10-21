class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        '''                                              ||
            ||                ||                         ||
            05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20
        '''
        count = Counter(nums)
        nums = sorted(count.keys())
        pref = [0] + list(accumulate([count[num] for num in nums]))
        ans, N = 1, len(nums)


        for num in range(nums[0], nums[-1] + 1):
            lb = bisect_left(nums, num - k)
            rb = bisect_right(nums, num + k)

            ans = max(
                ans,
                count[num] + min(pref[rb] - pref[lb] - count[num], numOperations)
            )

        return ans
