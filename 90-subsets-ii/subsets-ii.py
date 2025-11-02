class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        seen = set()

        for i in range(2**N):
            curr = []
            for num in nums:
                if i & 1:
                    curr.append(num)
                i >>= 1
            tp = tuple(curr)
            if tp not in seen:
                seen.add(tp)
                ans.append(curr)
        return ans
        