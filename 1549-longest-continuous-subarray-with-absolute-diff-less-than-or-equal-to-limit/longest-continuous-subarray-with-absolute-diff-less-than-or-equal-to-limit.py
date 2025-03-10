class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # use monotonic queue

        dec_stk = deque() # to get the max val so far
        inc_stk = deque() # to get the min val so far

        left, mx_size = 0, 0

        for right, curr in enumerate(nums):
            while dec_stk and nums[dec_stk[-1]] > curr:
                dec_stk.pop()
            dec_stk.append(right)

            while inc_stk and nums[inc_stk[-1]] < curr:
                inc_stk.pop()
            inc_stk.append(right)


            while nums[inc_stk[0]] - nums[dec_stk[0]] > limit:
                num = nums[left]

                if num == nums[dec_stk[0]]: dec_stk.popleft()
                if num == nums[inc_stk[0]]: inc_stk.popleft()

                left += 1
            mx_size = max(mx_size, right - left + 1)

        return mx_size


