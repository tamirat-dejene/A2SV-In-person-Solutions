class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans, N = set(), len(nums)

        for i in range(1, 2**N + 1):
            keep = []

            for j in range(N):
                if i & 1 and (not keep or keep[-1] <= nums[j]):
                    keep.append(nums[j])
                i >>= 1

            if len(keep) >= 2:
                ans.add(tuple(keep))

        return list(list(a) for a in ans)
        