class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # (n - i) * (i + 1): total possible # of subarrays including the current element at index i for n sized array

        min_stk = []
        ans = 0

        for i, num in enumerate(arr):
            # find the scope for which the current num will be min (to the left and to the right)
            while min_stk and num < arr[min_stk[-1]]:
                curr = min_stk.pop()
                l = curr - (-1 if not min_stk else min_stk[-1])
                r = i - curr

                ans = (ans + (l * r * arr[curr])) % (10**9 + 7)
            min_stk.append(i)

        
        # process the rest

        while min_stk:
            curr = min_stk.pop()
            l = curr - (-1 if not min_stk else min_stk[-1])
            r = len(arr) - curr
            ans = (ans + (l * r * arr[curr])) % (10**9 + 7)
        
        return ans
