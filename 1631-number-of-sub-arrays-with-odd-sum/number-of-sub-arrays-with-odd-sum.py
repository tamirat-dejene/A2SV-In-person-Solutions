class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans, rsum, evens, odds = 0, 0, 1, 0

        for num in arr:
            rsum += num
            rsum %= 2

            if rsum == 0: ans += odds
            else: ans += evens

            if rsum == 0: evens += 1
            else: odds += 1
    
        return ans % (10**9 + 7)